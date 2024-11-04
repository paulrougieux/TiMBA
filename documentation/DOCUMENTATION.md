<!-- TOC -->

- [Documentation of data, parameter, and model structure](#documentation-of-data-parameter-and-model-structure)
  - [Preface](#preface)
  - [Summary](#summary)
  - [Introduction](#introduction)
  - [Model formulation and specifications](#model-formulation-and-specifications)
    - [Demand:](#demand)
    - [Supply:](#supply)
    - [Manufacturing:](#manufacturing)
    - [Trade:](#trade)
  - [Countries and Products](#countries-and-products)
  - [Input Data and Parameter](#input-data-and-parameter)
    - [Structure / Organisation of Input Data](#structure--organisation-of-input-data)
  - [Parameter Development](#parameter-development)
    - [Exogenous changes](#exogenous-changes)
  - [Validation](#validation)
    - [Projection / historic data replication](#projection--historic-data-replication)
    - [Inter-model comparison](#inter-model-comparison)
    - [Economic shocks / economic behaviour](#economic-shocks--economic-behaviour)
  - [Annex](#annex)
    - [Parameter list](#parameter-list)

<!-- /TOC -->

Timber market Model for policy-Based Analysis

![TiMBA Logo](..\timba_logo_v3.png)

# Documentation of data, parameter, and model structure

authored by TI-FSM

TI-FSM is an authors’ collective that jointly developed and program TIMBA. The members of the collective are – in alphabetical order – Christian Morland, Franziska Schier, Julia Tandetzki, and Tomke Honkomp

## Preface
TIMBA is a partial economic equilibrium model for the global forest products market. The model endogenously simulates production, consumption and trade of wood and wood-based products in 180 countries. 
TIMBA  computes the market equilibrium for each country and product in a given period by maximizing the social surplus in the global forest sector. Intertemporal modeling is conducted through recursive simulations. In the equilibrium processes, product supply, demand and price are balanced for each simulation period. 
This work is the result of great joint efforts of the forest products market analysis team at the Thünen Institute of International Forestry and others from 2018 to 2024. In the recent, a number of people made important contributions to this work. Without their support, reflection, and constructive criticism, this undertaking would not have been as successful as it turns out to be now. We would like express our gratitude to all of them. In particular, we would like to thank 
- Pixida GmbH and especially Tobias Hierlmeier for professional support in revising and restructuring the model architecture and code and being valuable help in programming tasks
- Thünen Institute Service Centre for Research Data Management and especially Harald von Waldow for providing expertise, consultation and support during the release process
- Holger Weimar and Matthias Dieter for the trustful and cooperative working environment, rational support and critical discussion and the opportunity to keep going
- Johanna Schliemann for immediate technical support whenever needed
- The Thünen Institute of Forestry and its Head Matthias Dieter for providing financial resources over the years


## Summary
This working paper details the underlying structure of TIMBA as well as the data and parameters used for modelling. 
TIMBA is a partial economic equilibrium model for the global forest products market. The market equilibrium is subject to market clearance and constraints balancing necessary raw materials and produced wood products and limiting the trade (Samuelson 1952). The model structure distinguishes between raw, intermediate and end products. TIMBA differentiates three types of roundwood (wood fuel, coniferous and non-coniferous industrial roundwood), two additional raw products for paper production (other fibre pulp and waste paper), two intermediate products (mechanical and chemical pulp) and eight finished products (coniferous and non-coniferous sawnwoods, veneer sheets and plywood, particle board, fibreboard, newsprint, printing and writing paper, and other paper and paperboards). Except for sawnwoods, intermediate and end products are produced from a mix of coniferous and non-coniferous industrial roundwood. Scenario simulations with TIMBA are guided by parameters and assumptions shaping future developments. In the model framework, wood products are implicitly treated as perfect substitutes, regardless of their origin, as long as they belong to the same commodity group. 

As the optimization of the market equilibrium in a given year does not include an elasticity of substitution, demand is merely shifted by changes in income and price (Murray et al. 2004). The supply of roundwood depends on wood prices and forest development which in turn is basically determined by the growth dynamics of forest stock, the change in forest area, and harvest volumes. The GDP development indicating national incomes is an important driver of change. In TIMBA, demand for wood-based products is positively correlated to income, thus, an increase in income basically leads to an increase in demand. Forest area development and timber supply is coupled to GDP per capita developments based on the concept of the environmental Kuznets curve (Panayotou 2004). In its basic version, TIMBA uses the assumptions made in the “Middle of the road” scenario described in “The Shared Socioeconomic Pathways” (the so called SSP2 scenario) to model future GDP developments and population growth. This scenario describes a world of modest population growth and where social, economic and technological trends continue similarly to historical patterns (Riahi et al. 2017). Price and income elasticities of demand are taken from Morland et al. (2018). Further exogenous specifications on technology developments (input-output coefficients and manufacturing cost) are estimated based on historical developments from 1993-2020 while information on trade inertia and cost are based on WTO data as provided in the Forest Products Model (GFPM) (Buongiorno et al. 2015; GFPM version 1-29-2017-World500). The base year for the scenario simulations with the current version of TIMBA is 2020. The input data used for simulation with TIMBA needs to be calibrated and provided in a source file prior to model runs. This file is provided together with the model. The calibration procedure is described in Buongiorno and Zhu (2015) and altered according to Schier et al. (2018). The input data for calibrating the model are obtained from three global databases: The FAO forestry statistics (FAOSTAT), the FAO Forest Global Resources Assessment (FAO 2020) and the World Bank Development Indicators (World Bank). The model output comprises information about production, consumption and trade quantities, and prices as well as forest development. The model concept bases on the formal description of GFPM (Buongiorno et al. 2015, Buongiorno et al. 2003).

**Table X:** Modell characteristics

|Model type|Dynamic and static equilibrium market model|
|-----------------------------------| -----------------------------------|
|Geographical scope|Global (180 countries)|
|Temporal Dimension|Recursive long term analyses|
|Products|Raw-, intermediate, endproducts|
|Data sources|FAO, FRA, WDI, Comtrade|
|Software Implementation|Python 3.8, Python 3.9|
|Current code version|TiMBA 1.0.1|
|Permanent link to code repositiory|  |
|Code License| APGL3|
|Code versioning system used|GITHUB, Zenodo|
|Optimizer|OSQP|


[comment]: <> (add table)

## Introduction
This paper provides an overview over the data and parameters used in the TImber market Model for policy-Based Analsis (TIMBA) and gives an introduction to the model structure and specifications. Further, the results from validating the model performance are presented. 

TIMBA is a multi-periodic partial economic equilibrium model for the global forest products market. The model simulates production, imports, exports, consumption quantities and prices as well as technological and forest development for 16 commodities and 180 countries. The prices of wood and wood-based products are endogenous to the model. The market equilibrium is subject to market clearance and constraints balancing necessary raw materials and produced wood products and limiting the trade (Samuelson 1952). In the model framework, wood products are implicitly treated as perfect substitutes, regardless of their origin, as long as they belong to the same commodity. As the optimization of the market equilibrium in a given year does not include an elasticity of substitution, demand is merely shifted by changes in income and price (Murray et al. 2004).

TIMBA distinguishes between raw, intermediate and end products. The model structure currently includes three types of roundwood (wood fuel, coniferous and non-coniferous industrial roundwood), two additional raw products for paper production (other fibre pulp and waste paper), two intermediate products (mechanical and chemical pulp) and eight finished products (coniferous and non-coniferous sawnwoods, veneer sheets and plywood, particle board, fibreboard, newsprint, printing and writing paper, and other paper and paperboards). Commodities and commodity aggregates are determined by the definitions of UNECE (2021). Except for sawnwoods, intermediate and end products are produced from a mix of coniferous and non-coniferous industrial roundwood. Production of intermediate and end products is modelled using Input-Output coefficients determining the level of inputs needed for producing one unit of output. The production level depends on raw material prices, costs of manufacturing as well as commodity prices. While the prices of raw materials and intermediate and end-products are simulated endogenously, cost of manufacturing and transport are given exogenously. 

Demand for wood-based products is tied to country-specific income (GDP) and price levels via price and income elasticities taken from Morland et al. (2018). In TIMBA, demand for wood-based products is positively correlated to income, thus, an increase in income basically leads to an increase in demand while demand decreases with increasing product price. 

The supply of roundwood depends on wood prices and stock volume which in turn is determined by the growth dynamics of forest stock, the change in forest area, and harvest volumes. TIMBA model import from and to one singlecountry to the world. Trade occurs when the price of a product in a certain country exceeds the foreign price plus transport costs or vice versa is lower   than the world price. Simultaneously, there is a need for trade due to the scarcity of goods in one country, which leads in an increased demand or, conversely, an increased supply leading to a surplus in another country.   This dynamic consequently incentivizes international trade as countries attempt to balance their supply and demand through imports and exports. The difference in production costs and prices between countries further reinforce the need for such trade interactions in order to optimize resource allocation and market equilibrium. 

Scenario simulations with TIMBA are guided by parameters and assumptions shaping future developments. The GDP development indicating national incomes is an important driver of change. In its basic version, TIMBA uses the assumptions made in the “Middle of the road” scenario described in “The Shared Socioeconomic Pathways” (the so called SSP2 scenario) to model future GDP developments and population growth. This scenario describes a world of modest population growth and where social, economic and technological trends continue similarly to historical patterns (Riahi et al. 2017). Demand is subject to annual changes following the projected GDP growth and endogenous price developments, so that new prices and income levels shift the demand for wood-based products via elasticities at an annual interval. On the supply side, price and volume elasticities shift the wood supply at an annual interval. Forest area development and thus, stock volume and timber supply are coupled to GDP per capita developments based on the concept of the environmental Kuznets curve (Panayotou 2004). Information on trade inertia and cost are based on WTO data as provided in the GFPM (Buongiorno et al. 2015; GFPM version 1-29-2017-World500). The base year for the scenario simulations with the current version of TIMBA is 2020. The input data used for simulation with TIMBA needs to be calibrated and provided in a source file prior to model runs. This file is provided together with the model. The calibration procedure is described in Buongiorno and Zhu (2015) and altered according to Schier et al. (2018). The input data for calibrating the model are obtained from three global databases: The FAO forestry statistics (FAOSTAT), the FAO Forest Global Resources Assessment (FAO 2020) and the World Bank Development Indicators (World Bank). The model output comprises information about production, consumption and trade quantities, and prices as well as forest development and technologie?

The model concept bases on the formal description of the Global Forest Products Model (GFPM) (Buongiorno et al. 2015, Buongiorno et al. 2003).

![Caption for example figure.\label{fig:1}](..\images\timba_product_transformation.png)

**Figure 1:** Material flow and product structure in TIMBA. Other Fiber Pulp and Waste Paper are solely inputs in the paper sector. Wood residues used as input in the wood-based panel and pulp sectors are not explicitly modeled in TIMBA but implicitly considered by manufacturing coefficients. Double represent the mix of raw materials as input for further processing. Thus, wood-based panels could be made from a single input or a mixture of coniferous and non-coniferous roundwood while paper products could be made from a single input or a mixture of pulp and waste paper. The dotted lines indicate that other industrial roundwood is composite product: While raw data are imported for data calibration, the amounts of coniferous and non-coniferous other industrial roundwood are calculated out from of the total amount of industrial roundwood and summed up as total other industrial roundwood for model simulation. The bold lines indicate, that the product is not further processed before sold as end product.

## Model formulation and specifications
TiMBA computes periodical production, import, exports and demand quantities as well as prices for the forest-based sector considering forest resources as well as, cost, technology and trade constraints.  The recursive market model consists of a static and a dynamic phase. In the static phase, TiMBA calculates a global equilibrium across all products and countries in a given year. The modelling problem is solved recursively for each year by maximizing the economic welfare, defined as the sum of the producer and consumer economic surplus.. The model calibration for Timba follows the procedure as formally described in Buongiorno (2015) and refined by Schier et al. (2018). Currently, the calibration procedure is not included int the TiMBA package. The calibrated data are provided as input for simulations together with the model under www.git... 

In the dynamic phase, changes in the equilibrium conditions (shifts in parameters determining the model outcome such as growing GDP, population or cost) are updated from one period to the next.

The model concept bases on the formal description of the Global Forest Products Model (GFPM) [@Buongiorno:2015;@Buongiorno:2003]. The following problem is optimized by using the CVXPY [@Diamond:2016; @Agrawal:2018] package and the OSQP solver [@Stellato:2020]:

$$\max_{Z}=\sum_{i}\sum_{k}\int_{0}^{D_{i,k}}P_{i,k}\left(D_{i,k}\right)dD_{i,k}-\sum_{i}\sum_{k}\int_{0}^{S_{i,k}}P_{i,k}\left(S_{i,k}\right)dS_{i,k}$$
$$-\sum_{i}\sum_{k}\int_{0}^{Y_{i,k}}m_{i,k}\left(Y_{i,k}\right)dY_{i,k}-\sum_{i}\sum_{j}\sum_{k}c_{i,j,k}T_{i,j,k}$$

with $P$ as price, $D$ as demand, $S$ as supply, $Y$ as manufacturing, $m$ as manufacturing costs, $T$ as trade, $c$ as transportation costs and the indeces $i$ for country, $j$ as trade partner country and $k$ as commodity.

Subject to:
$$S_{i,k}+Y_{i,k}+\sum_{j}I_{j,k}=D_{i,k}+\sum_{n}a_{i,k,n}Y_{i,n}+\sum_{j}X_{j,k}$$

### Demand:

The demand for wood-based products is correlated to income ($y$) and wood prices. 

$$P_{i,k}(D_{i,k}) = P_{i,k,t-1}\left(\frac{D_{i,k}}{D^{*}_{i,j}}\right)^{1/\delta_{i,k}}$$

$$D_{i,k}^{*}=D_{i,k,t-1}\left(1+\alpha_{y}g_{y}+\alpha_{D,t-1}g_{D,t-1}+\alpha_0\right)$$

with $\delta$ as damand price elasticity, $g_y$ as growth rate of income, $g_D$ as exogenous growth rath of demand, $\alpha$ as exogenous parameters to shift the influence of the growth rates and t as time index.


### Supply:

The supply of roundwood depends on wood prices and forest development which in turn is basically determined by the growth dynamics of forest stock, the change in forest area, and harvest volumes:

$$P_{i,k}(S_{i,k}) = P_{i,k,t-1}\left(\frac{S_{i,k}}{S^{*}_{i,j}}\right)^{1/\lambda_{i,k}}$$

$$S_{i,k}^{*}=S_{i,k,t-1}\left(1+\beta_{y}g_{y}+\beta_{I}g_{I}\right)$$

with $\lambda$ as supply price elasticity, $g_y$ as growth rate of income, $g_I$ as growth rate of forest inventory and $\beta$ as exogenous paramters to shift the influence of the growth parameters.

Forest area development and thus, timber supply is coupled to GDP per capita developments based on the concept of the environmental Kuznets curve (Panayotou 2004). 

[comment]: <> (Panayotou 2004 als Bibtext Referenz in .bib )

$$g_{I}=\left(1+\gamma_0\left(\frac{I_{t-1}}{A_{t-1}}\right)^\sigma+\left(\alpha_0+\alpha_{1}y^{'}\right)e^{\alpha_{2}y^{'}}\right)$$

with $I$ as forest inventory, $A$ as forest area, $\sigma$ as elasticity of inventory per unit area, $y^{'}$  as per capita income and $\gamma$ and $\alpha$ as exoenous paramters to shift the growth rates.

### Manufacturing:

$$m_{i,k}(Y_{i,k}) = m^{*}_{i,k,t-1}\left(\frac{Y_{i,k}}{Y_{i,j,t-1}}\right)^{\zeta_{i,k}}$$

$$m^{*}_{i,k}=m_{i,k,t-1}\left(1+g_m\right)$$

with $\zeta$ as manufacturing cost elasticity and $g_m$ as growth rate of manufacturing costs.

### Trade:

$$c_{i,j,k}(T_{i,j,k}) = c^{*}_{i,j,k,t-1}\left(\frac{T_{i,j,k}}{T_{i,j,k,t-1}}\right)^{\tau_{i,j,k}}$$

$$c^{*}_{i,j,k}=c_{i,j,k,t-1}\left(1+g_f+g^i_t+g^x_i\right)$$

with $\tau$ as transportation cost elasticity, $g_f$ as growth rate of freight costs, $g_t^i$ as growth rate of import taxes and $g_t^x$ as growth rate of export taxes.

## Countries and Products
For each of the 180 countries considered in the model, TiMBA includes three main sectors along the forest-based value chain: the forestry sector, the wood-processing based industries and the consumers of forest-based products. The forestry sector provides the forest resources to supply Fuelwood as well as coniferous, non-coniferous and other industrial roundwood. Forest industries then transform coniferous and non-coniferous industrial roundwood into intermediate and end products which are either used as input for, e.g., paper production or demanded by consumer markets. 

Beyond four types of roundwood, the product structure in TiMBA further distinguishes coniferous and non-coniferous sawnwood, plywood and veneer sheets, particle board including OSB, fibre board, newsprint, printing and writing paper and other paper and paper board as end products as well as mechanical and chemical pulp (including semi-chemical pulp) as intermediate and other fibre pulps and waste paper as additional raw materials. For this products TiMBA simulates the production, import, export and demand and prices in each year for each country. As shown in table x, not every product is subject to trade, manufacturing or consumer demand. 

## Input Data and Parameter

### Structure / Organisation of Input Data 

TiMBA uses input data and parameter from various sources. Data on country-specific production and trade quantities of raw, intermediate, and end products are taken from FAOSTAT. 

Product consumption for the base year is then calculated as production + imports – exports. Further, data on country-specific export values from FAOSTAT are used to compute unit product prices in the base year as the total export volume divided by total export quantity stated in constant US $.  … Prices are deflated for the base year using the GDP deflator from World Development Indicators database, Code NY.GDP.DEFL.ZS. Unit prices differ for net-importer and net-exporter countries. The unit price of net-importers of a given commodity is the export unit price plus commodity specific freight costs and tariffs. 

Tariffs are derived from WTO Integrated Database (IDB) notifications as average of ad valorem duties for the last current year available of the respective reporter country and product on HS-code level 4 – 6. Freight cost are calculated as freight factor times export unit value. Freight factors are taken from GFPM urlalt / Buongiorno xxx (add Table?).  
It is assumed that the consumption of one product (C) depend on the price of the product and the domestic income in form of GDP. These relations are represented by elasticities of demand. On the supply side it is assumed that wood supply equals the removals from forests. It is driven by prices of raw materials as well as the forest stock density of a respective country and represented by respective elasticities. Supply of wastepaper and other fibre pulp depends on product prices and national income (GDP). All elasticities are summarized in Table ab.

[comment]: <> (add tables)

**Table x:** Items simulated with TiMBA. Product definitions according to FAOSTAT and FAO Forest resources assessment (Quellen) 

|Item|Unit|Supply|Production|Demand|Trade|Price|Growth|
|:------------------|:-------:|:-:|:-:|:-:|:-:|:-:|:-:| 
|Fuelwood                  | 1000 m³  |x| |x|x|x| |
|Industrial Roundwood C    | 1000 m³  |x| | |x|x| |   
|Industrial Roundwood NC   | 1000 m³  |x| | |x|x| | 
|Oth Industrial Roundwood  | 1000 m³  |x| |x| | | |
|Coniferous Sawnwood       | 1000 m³  | |x|x|x|x| | 
|Non-coniferous Sawnwood   | 1000 m³  | |x|x|x|x| |
|Plywood and Veneer Shets  | 1000 m³  | |x|x|x|x| | 
|Particle Board (incl. OSB)| 1000 m³  | |x|x|x|x| |
|Fibre Board               | 1000 m³  | |x|x|x|x| |
|Mechanical Pulp           | 1000 t   | |x| |x|x| |
|Semi chem. and Chem. Pulp | 1000 t   | |x| |x|x| |
|Other Fibre Pulp          | 1000 t   |x|x| |x|x| |
|Waste Paper               | 1000 t   |x| | |x|x| |
|Newsprint                 | 1000 t   | |x|x|x|x| |
|Print. and Writing Paper  | 1000 t   | |x|x|x|x| |
|Other Paper and Paperb.   | 1000 t   | |x|x|x|x| |
|Forest Area               | ha       | | | | | |x|
|Forest Stock              |million m³| | | | | |x|

<br><br>

![timba_countries](..\images\timba_country_coverage.png)
**Figure y:** Countries which are included in TiMBA

[comment]: <> (CM: ich würde vorschlagen eher eine Grafik einzubauen als die große Tabelle, oder aber die Tablle mit ISO3 Codes versehen.)

**Table x:** List of 180 countries included into forest sector modelling

|                       |                       |                       |                       |
| --------------------- | --------------------- | --------------------- | --------------------- |
|Algeria                |El Salvador            |  Maldives             |St.Vincent/Grenadines  |
|Afghanistan            |Equatorial Guinea      |  Mali                 |        Sudan          |
  |Albania            |Estonia          |Martinique        |Suriname               |
  |Angola             |Ethiopia         |Mauritania        |Swaziland              |
 |Argentina          |Fiji Islands     |Mauritius          |Sweden                 |
  |Armenia            |Finland          |Mexico            | Switzerland           |
  |Australia          |France           |Moldova, Republic |Syrian Arab Republic   |    
  |Austria            |French Guiana    |Mongolia          |Tajikistan             |
  |Azerbaijan,Republic|French Polynesia |Montenegro        |Tanzania, United Rep of|                                         
  |Bahamas           |Gabon            |Morocco            |Thailand               |
  |Bahrain            |Gambia           |Mozambique        |Timor-Leste            |
  |Bangladesh         |Georgia          |Myanmar           |Togo                   |
  |Barbados           |Germany          |Nepal             |Tonga                  |
  |Belarus            |Ghana            |Netherlands       |Trinidad and Tobago    |
  |Belgium            |Greece           |Netherlands Antilles|Tunisiav              |
  |Belize             |Guatemala        |New Caledonia     |Turkey                 |
  |Benin              |Guinea           |New Zealand       |Turkmenistan           |
  |Bhutan             |Guinea-Bissau    |Nicaragua         |Uganda                 |
  |Bolivia            |Guyana           |Niger             |Ukraine                |
  |Bosnia and Herzegovina|Haiti            |Nigeria           |United Arab Emirates   |                    
  |Botswana           |Honduras         |Norway            |United Kingdom         |
  |Brazil             |Hungary          |Oman              |Uruguay                |
  |Brunei Darussalam  |India            |Pakistan          |USA                    |
  |Bulgaria           |Indonesia        |Panama            |Uzbekistan             |
  |Burkina Faso       |Iran, Islamic Rep of|Papua New Guinea  |Vanuatu                |                       
  |Burundi            |Iraq             |Paraguay          |Venezuela, Boliv Rep of|
  |Cambodia           |Ireland          |Peru              |Viet Nam             |
  |Cameroon           |Israel           |Philippines       |Yemen                |
  |Canada             |Italy            |Poland            |Zambia               |
  |Cape Verde         |Jamaica          |Portugal          |Zimbabwe             |
  |Central African Republic|Japan            |Qatar             |                     |                                
  |Chad               |Jordan           |Réunion           |                     |
  |Chile              |Kazakhstan       |Romania           |                     |
  |China              |Kenya            |Russian Federation|                     |
  |Colombia           |Korea, Dem People\'s Rep|Rwanda            |                     |         
  |Congo, Dem Republic of|Korea, Republic of|Saint Lucia       |                     |                     
  |Congo, Republic of |Kuwait           |Samoa             |                     |
  |Cook Islands       |Kyrgyzstan       |Sao Tome and Principe|                     |
  |Costa Rica         |Laos             |Saudi Arabia      |                     |
  |Côte d\'Ivoire     |Latvia           |Senegal           |                     |
  |Croatia            |Lebanon          |Serbia            |                     |
  |Cuba               |Lesotho          |Sierra Leone      |                     |
  |Cyprus             |Liberia          |Singapore         |                     |
  |Czech Republic     |Libya            |Slovakia          |                     |
  |Denmark            |Lithuania        |Slovenia          |                     |
  |Djibouti           |Luxembourg       |Solomon Islands   |                     |
  |Dominica           |Macedonia        |Somalia           |                     |
  |Dominican Republic |Madagascar       |South Africa      |                     |
  |Ecuador            |Malawi           |Spain             |                     |
  |Egypt              |Malaysia         |Sri Lanka         |                     |


**Table x:** Demand and supply elasticities

|                         |Demand elasticity   || Supply elsaticity            |||
|-------------------------|:--------:|:--------:|:--------:|:--------:|:--------:|
| Commodity               | price    | income   | price    | income   |forest stock|
| Fiberboard              | -0.4629  | 1.0661   |          |          |         |
| Fuelwood                | -0.1458  | 0.5680   |          |          |         |
| Newsprint               | -0.1208  | 0.2371   |          |          |         |
| Other Paper             | -0.1695  | 0.2283   |          |          |         |
| P. & W. Paper           | -0.5188  | 0.3626   |          |          |         |
| Particle Board          | -0.4923  | 0.7502   |          |          |         |
| Plywood & Veneer        | -0.3534  | 0.596    |          |          |         |
| Sawnwood C              | -0.3001  | 0.4409   |          |          |         |
| Sawnwood NC             | -0.1221  | 0.2162   |          |          |         |
| Fuelwood                |          |          | 1.0311   | \-       | 1.1000  |
| Industrial Roundwood C  |          |          | 1.0738   | \-       | 1.1000  |
| Industrial Roundwood NC |          |          | 1.0440   | \-       | 1.1000  |
| Wastepaper              |          |          | 1.0000   | 0.1400   | \-      |
| Other Fibre Pulp        |          |          | 1.0000   | 0.1400   | \-      |

Note: This is a summarizing table; Elasticities are shown for the best model, which is chosen on the basis of Breusch-Pagan, Maddala-Wu and Hausman tests based on Morland et al. 2018 "taken from GFPM (Buongiorno et al. 2003) version 2020  (World 500)

## Parameter Development
### Exogenous changes

Computer software

After local linear approximation of the demand, supply and cost functions (2), (3) and (7), the objective function (1) is quadratic in D, S, Y and T. Thus, the equilibrium in a given year is obtained by solving a quadratic optimization problem with linear constraints. The solution is computed with an interior point solver (BPMPD, Me´sza´ ros, 1999). The GFPM input and output for calibration and simulation is facilitated by Excel spreadsheets and graphics. A recent version of the complete software, its documentation and a pre-calibrated dataset are available freely for academic research (Buongiorno and Zhu, 2014a,b)

## Validation


### Projection / historic data replication


### Inter-model comparison


### Economic shocks / economic behaviour 


## Annex


### Parameter list

