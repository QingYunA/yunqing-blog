---
title: Enabling Large Language Models (LLMs) to Understand Tree-like JSON Structures via TypeScript Syntax
published: 2025-08-21
description: Enabling Large Language Models (LLMs) to Understand Tree-like JSON Structures via TypeScript Syntax
tags: [Large Language Models, Tree-like JSON, Understanding, LLMs, TypeScript]
category: Tools
draft: false
---

## Motivation
Recently, in my work, I needed to extract tree-like JSON structures from a large amount of text data.  
Existing methods for making large language models output JSON generally involve setting `response_format` to `json_object`, which works well when the keys in the output example are fixed. For example:  
```json
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
```
However, when the keys are dynamic, it is difficult to accurately convey a tree-like structure (which can extend infinitely) with variable key names and values using natural language.  
> It is challenging to describe a node tree like the one below using natural language or JSON format.

![](https://s2.loli.net/2025/08/21/BnHjmyk87Q4RdDL.png)

## Describing Node Trees Using TypeScript Syntax

After researching, I discovered that using TypeScript's `interface` type to describe the desired tree can help large language models understand the nested structure of the tree, and it offers richer expressiveness.  
### Reference Prompt
- Please return JSON data strictly following this `Tree` interface:
```ts
type Tree = {
  [firstLevelNode: string]: {
    [secondLevelNode: string]: Level2Node;
  };
};

interface Level2Node {
  "Node Description": string;
  "Node Tasks": string[];
  // Use XXX condition as a branch to enter deeper recursive nodes
  [branchCondition: string]: DeepNode;
}

interface DeepNode {
  "Node Description": string;
  "Node Tasks": string[];
  "Node Content"?: string[] | string;
  [branchCondition: string]: DeepNode;
}
```

- In the prompt, you can use `string` or `string[]` to indicate whether the value under this key should be a pure string or an array of strings. You can also use `?` to indicate that the key is optional.
- You can use the `|` symbol to represent multiple optional types.

## Summary
In fact, there should also be methods based on `JSON Schema` for specification. However, at the time, I found limited resources on this approach and instead developed this TypeScript syntax-based method through experimentation, which has proven highly effective. I hope this can be helpful to readers who need to instruct LLMs to generate JSON.