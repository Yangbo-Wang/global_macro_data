# The Global Macro Database (Python Package)
<a href="https://www.globalmacrodata.com" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Website-Visit-blue?style=flat&logo=google-chrome" alt="Website Badge">
</a>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Link to paper 📄](https://www.globalmacrodata.com/research-paper.html)



This repository complements our paper, **Müller, Xu, Lehbib, and Chen (2025)**, which introduces a panel dataset of **46 macroeconomic variables across 243 countries** from historical records beginning in the year **1086** until **2024**, including projections through the year **2030**.




## Features

- **Unparalleled Coverage**: Combines data from **32 contemporary sources** (e.g., IMF, World Bank, OECD) with **78 historical datasets**.
- **Extensive Variables**: GDP, inflation, government finance, trade, employment, interest rates, and more.
- **Harmonized Data**: Resolves inconsistencies and splices all available data together.
- **Scheduled Updates**: Regular releases ensure data reliability.
- **Full Transparency**: All code is open source and available in this repository.
- **Accessible Formats**: Provided in `.dta`, `.csv`, `.xlsx`and as **Stata/Python package**.

## Data access

<a href="https://www.globalmacrodata.com/data.html" target="_blank" rel="noopener noreferrer">Download via website</a>

**Python package:**
```
pip install global_macro_data
```

**How to use (an example)**
```
import global_macro_data as gmd
df = gmd.get_data(start_year=2000, end_year=2010, country=['United States','France','Germany','China'])
# You can also use ISO3 for retrieval.
df = gmd.get_data(start_year=2000, end_year=2010, ISO3=['USA','FRA','DEU','CHN'])
```

## Parameters
- **start_year (int)**: Filter data from this starting year (inclusive).
- **end_year (int)**: Filter data up to this ending year (inclusive).
- **country (str, list, or comma-separated string)**: Filter data by country name(s).
- **ISO3 (str or list)**: Filter data by ISO3 country code(s).
- **format (str)**: Data format, either 'csv' or 'xlsx'.

## Release schedule 

| Release Date | Details          |
|--------------|------------------|
| 2025-01-30   | Initial release: v2025-01 |
| 2025-04-01   | v2025-04         |
| 2025-07-01   | v2025-09         |
| 2025-10-01   | v2025-12         |
| 2026-01-01   | v2026-03         |



## Citation

To cite this dataset, please use the following reference:

```bibtex
@techreport{mueller2025global, 
    title = {The Global Macro Database: A New International Macroeconomic Dataset}, 
    author = {Müller, Karsten and Xu, Chenzi and Lehbib, Mohamed and Chen, Ziliang}, 
    year = {2025}, 
    type = {Working Paper}
}
```

## Acknowledgments

The development of the Global Macro Database would not have been possible without the generous funding provided by the Singapore Ministry of Education (MOE) through the PYP grants (WBS A-0003319-01-00 and A-0003319-02-00), a Tier 1 grant (A-8001749- 00-00), and the NUS Risk Management Institute (A-8002360-00-00). This financial support laid the foundation for the successful completion of this extensive project.
