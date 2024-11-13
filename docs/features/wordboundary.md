# [BHSaddons](https://github.com/tonyjurg/BHSaddons) feature: wordboundary

Feature type | Data type | Available for node types
---  | --- | --- 
`Node`|`String`|`word`

## Feature description

This feature indicates wordboudaries (spaces OR maqaf). The maqaf (מַקָּף‎) functions in Hebrew to connect two words.

## Feature values

Either the number '1' (string) or empty. Frequency table for this feature:

Value | Description | Frequency
---|---|---
&lt;empty&gt;|not the last node in a word|
1|last node in a word|
