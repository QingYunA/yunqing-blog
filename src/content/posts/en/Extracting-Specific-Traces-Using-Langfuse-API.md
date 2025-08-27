---
title: Extracting Specific Traces Using Langfuse API
published: 2025-08-22
description: Extracting trace logs for specific traces using Langfuse API
tags: [langfuse, api, trace, log]
category: Learning
draft: false
---

# Extracting Trace Logs for Specific Traces Using Langfuse API

## Background
During development, I needed to batch retrieve logs for specific traces, but Langfuse's UI doesn't support batch downloading specific traces as JSON files. Here's a brief introduction on how to achieve this using the Langfuse API.

## Obtaining sessionId
A sessionId is required to retrieve all traces corresponding to that particular session batch.
The method is simple: in the Langfuse UI interface, locate the `sessionId` column in the traces section and copy it out.

## Obtaining Langfuse Keys and BASE_URL
In the Langfuse UI's `Settings`, find `API Keys`, create an API key. You'll obtain two keys: PUBLIC_KEY and SECRET_KEY, both of which need to be recorded.

If your Langfuse is on the public network, the BASE_URL is `https://api.langfuse.com/api/public/`. If your Langfuse is local, the BASE_URL is `http://YOUR_HOST/api/public/`.

## Relevant Code
Finally, write the `sessionId`, `PUBLIC_KEY`, `SECRET_KEY`, and `BASE_URL` into `langfuse_api.py`, then run `langfuse_api.py` to obtain the logs for the specified traces.

```python
import requests
import json

# Configuration
PUBLIC_KEY = ""
SECRET_KEY = ""
BASE_URL = "http://10.65.171.100:33000/api/public/"

# Target message_id to filter
TARGET_MESSAGE_ID = "17400353"
PAGE_SIZE=100

# Store results
results = 0
page = 1
has_more = True
target_date = "2025-08-06"
hour = 18


while has_more:
    print(f"📌 Fetching page {page} ({PAGE_SIZE} items per page)...")
    
    url = f"{BASE_URL}/traces"
    response = requests.get(
        url,
        auth=(PUBLIC_KEY, SECRET_KEY),
        params={
            "page":page,
            "limit":PAGE_SIZE,
            "sessionId":"test_cases_fivedoctors_20250806185514"
        },
    )
    res = response.json()


    if response.status_code != 200:
        print(f"❌ Request failed: {response.status_code} - {response.text}")
        break

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("❌ Response content is not JSON format, possibly network issue or address error")
        print("Response content:", response.text)
        break

    if isinstance(data, list):
        traces = data
        has_more = len(traces) == PAGE_SIZE  # If exactly full page, there might be more
    else:
        traces = data.get("data", [])
        current_page_size = len(traces)
        has_more = current_page_size == PAGE_SIZE

    for trace in traces:
        metadata = trace.get("metadata") or {}
        id = metadata["message_id"]
        with open(f'./result/{id}.json',"w",encoding="utf-8") as f:
            json.dump(trace, f, indent=2, ensure_ascii=False)
            results+=1
        

    if len(traces) < PAGE_SIZE:
        has_more = False

    page += 1

