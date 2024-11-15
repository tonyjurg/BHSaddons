[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14051603.svg)](https://doi.org/10.5281/zenodo.14051603) [![SWH](https://archive.softwareheritage.org/badge/origin/https://doi.org/10.5281/zenodo.14051603)](https://archive.softwareheritage.org/browse/origin/https://doi.org/10.5281/zenodo.14051603) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)




# BHSaddons

This repository offers a set of features built specifically for use with the [BHSA Text-Fabric dataset](https://github.com/ETCBC/bhsa). Text-Fabric is a powerful platform for analyzing biblical texts with linguistic and structural detail. To complement this, our this feature set focus on the parashot, the weekly portions into which the Torah is divided. A parasha is a designated section of the Torah, read during weekly synagogue services. Together, the 54 parashot divide the entire five books of the Torah, forming a yearly cycle of reading that is central to Jewish liturgy and tradition.

The following features are provided:

Feature name | Data type | Available on node | Description | Examples
---|---|---|---|---
[aliyotnum](docs/features/aliyotnum.md)| `Integer`| `verse` | Sequence number of the aliyot within the parasha | `1` ... `7` <span>` `</span>
[maftir](docs/features/maftir.md)|`String`| `verse` | Set to '1' if this verse is part of a maftir | <span>` `</span> `1`
[parashahebr](docs/features/parashahebr.md)|`String`| `verse` | The name of the parasha in Hebrew | `בְּרֵאשִׁית` `נֹחַ`
[parashanum](docs/features/parashanum.md)|`Integer`| `verse` | The sequence number of the parasha | `1` ... `54` &lt;empty&gt;
[parashatrans](docs/features/parashatrans.md)|`String`| `verse` | Transliteration of the Hebrew parasha name | `Bereshit` `Noach`
[parashaverse](docs/features/parashaverse.md)|`Integer`| `verse` | The sequence number of the verse within the parasha | `1` `2` ...
[wordboundary](docs/features/wordboundary.md)|`String`| `word` | This feature indicates wordboudaries (spaces OR maqaf)|  `1` <span>` `</span>


## Adding the features

By default, the additional features of the BHSA Text-Fabric dataset are not loaded. To include them, use the `mod` option during invocation, as shown below:

```python
# Load the BHSA app and data with additional parasha features
A = use ("etcbc/BHSA", version="2021", mod="tonyjurg/BHSaddons/tf/", hoist=globals())
```

To use this functionality, the Text-Fabric package must support downloading files from GitHub. If it was installed without GitHub functionality, you might encounter errors like the following when trying to load the additional features:

```
The requested data is not available offline
	~/text-fabric-data/github/tonyjurg/BHSaddons/tf/2021 not found
Backend provider github not supported.
Cannot reach online data on github
Try installing text-fabric one of the following:
pip install text-fabric[github]
pip install text-fabric[all]
```

To resolve this issue, ensure that GitHub support is added to Text-Fabric by running:

```
!pip install text-fabric[github]
```

Since GitHub implemented a API rate limit of 60 requests per hour, it is recommended to use a personal access token to increase this rate limit. Refer to the following resources for guidance:
- [Jupyter Notebook: Increase GitHub API Rate Limit](https://nbviewer.org/github/CenterBLC/N1904/blob/main/docs/tutorial/Increase_GitHub_rate_limit.ipynb)
- [Text-Fabric Documentation: Using GitHub Tokens](https://annotation.github.io/text-fabric/tf/advanced/repo.html#token-in-environment-variables)

## Example use case

The following python snippet allows for easy selection of all verse nodes of the first parasha, Bereshit.

```python
# find all word nodes for parasha Bereshit
parashaQuery = '''
verse parashatrans=Bereshit
  word
'''
parashaResults = A.search(parashaQuery)
for verse, node in parashaResults:
    # do some interesting stuff ...
```
  
