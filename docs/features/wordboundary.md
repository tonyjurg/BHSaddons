# BHSaddons feature: wordboundary

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

The following image shows the mapping of the surface text word to the `word` nodes in the BHSA Text-Fabric dataset, taking Genesis 1:1 as an example.

<img src="images/wordboundary.png">

The image shows that the first Hebrew word (בְּרֵאשִׁ֖ית) maps to two `word` nodes in Text-Fabric: node 1 for the 'בְּ' and node 2 for the 'רֵאשִׁ֖ית' part. In order to clearly mark the surface level wordboundaries, the feature value for wordboundary is set to 'empty' for node 1 and set to '1' for node 2.

