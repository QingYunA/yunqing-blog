---
title: 通过TypeScript语法让大模型(LLMs)理解树形json结构
published: 2025-08-21
description: 通过TypeScript语法让大模型(LLMs)理解树形json结构
tags: ['大模型', '树形json', '理解', 'LLMs', 'TypeScript']
category: 工具
draft: False
slug: 通过typescript语法让大模型llms理解树形json结构
---

## 动机
最近在工作中需要针对大量的语料去抽取出树形json结构。
现有的让大模型输出json的方法一般是设置`response_format`为`json_object`，在你指定输出样例的key是固定的时候，能够起到很好的效果。比如：
```json
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
```
但是当key是动态的时候，你很难通过自然语言准确的传达出一个key名、value可变的树形结构(可以无限延伸)。
> 下图这样的节点树很难用自然语言或者json格式描述出来

![](https://s2.loli.net/2025/08/21/BnHjmyk87Q4RdDL.png)

## 基于TypeScript语言描述节点树

经过搜索资料发现了采用`typescript`的`interface`类来描述你想要的树，可以让大模型理解树的嵌套结构,而且有更多丰富的表达。
### 参考prompt
- 请返回json数据，并严格遵循这个`Tree`interface
```ts
type Tree = {
  [一级节点: string]: {
    [二级节点: string]: Level2Node;
  };
};

interface Level2Node {
  "节点描述": string;
  "节点任务": string[];
  // 以XXX条件作为分支，进入更深层递归节点
  [分支条件: string]: DeepNode;
}

interface DeepNode {
  "节点描述": string;
  "节点任务": string[];
  "节点内容"?：string[] | string;
  [分支条件: string]: DeepNode;
}
```

- 在prompt中，可以通过string或string[]来告诉模型，希望在这个key下的value是纯字符串还是字符串数组，也可以使用?来表示这个key是一个可选key。
- 可以使用`|`符号表示多个可选类型

## 总结
事实上应该还有基于`json schema`方式的指定方式，但是笔者当时搜索了资料较少，自己摸索出来的基于typescript语法的方式有非常显著的成效，所以一直在使用这个方法，希望可以对需要指定llm生成json的读者有所帮助