[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

# BHSaddons

This repository contains a set of additional features developed for the [BHSA Text-Fabric dataset]().

The following features are provided:

feature | Description
---|---
[aliyotnum](docs/features/aliyotnum.md)|Sequence number of the aliyot within the parasha
[maftir](docs/features/maftir.md)| Set to '1' if this verse is part of a maftir
[parashahebr](docs/features/parashahebr.md)| The name of the parasha in Hebrew
[parashanum](docs/features/parashanum.md)| The sequence number of the parasha
[parashatrans](docs/features/parashatrans.md)| Transliteration of the Hebrew parasha name
[parashaverse](docs/features/parashaverse.md)| The sequence number of the verse within the parasha


# Adding the features

By default, the additional features of the Nestle 1904 Text-Fabric dataset are not loaded. To include them, use the `mod` option during invocation, as shown below:

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
