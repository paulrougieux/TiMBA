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
    - [Forest](#forest)
  - [Countries and Products](#countries-and-products)
  - [Input Data and Parameter](#input-data-and-parameter)
    - [Overview on Input Data](#overview-on-input-data)
    - [Overview on Parameters](#overview-on-parameters)
    - [Exogenous Parameter Development](#exogenous-parameter-development)
  - [Computer software](#computer-software)
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

TI-FSM is an authors’ collective that jointly developed and program TiMBA. The members of the collective are – in alphabetical order – Christian Morland, Franziska Schier, Julia Tandetzki, and Tomke Honkomp

## Preface
TIMBA is a partial economic equilibrium (PE) model for the global forest products market. The model endogenously simulates production, 
consumption and trade of wood and wood-based products in 180 countries. 
TIMBA  computes the market equilibrium for each country and product in a given period by maximizing the social surplus in the global forest sector. 
Intertemporal modeling is conducted through recursive simulations. In the equilibrium processes, commodity production, consumption and prices are balanced 
for each simulation period. 
This work is the result of great joint efforts of the forest sector modelling team at the Thünen Institute of Forestry from 2018 to 2024. 
In recent years, a number of people made important contributions to this work. Without their support, reflection, and constructive criticism, 
this undertaking would not have been as successful as it turns out to be now. We would like express our gratitude to all of them. 
In particular, we would like to thank 
- Pixida GmbH and especially Tobias Hierlmeier for professional support in revising and restructuring the model architecture and code and being valuable help in programming tasks
- Thünen Institute Service Centre for Research Data Management and especially Harald von Waldow for providing expertise, consultation and support during the release process
- Holger Weimar and Matthias Dieter for the trustful and cooperative working environment, rational support and critical discussion and the opportunity to keep going
- Johanna Schliemann for immediate technical support whenever needed
- The Thünen Institute of Forestry and its Head Matthias Dieter for providing financial resources over the years


## Summary
This working paper details the underlying structure of TiMBA as well as the data and parameters used for modelling. 
TiMBA is a partial economic equilibrium model for the global forest sector. The market equilibrium is subject to 
market clearance and constraints balancing raw material, product manufacturing, consumption while limiting international 
trade [@Samuelson:1952]. The model structure distinguishes between raw, intermediate and end products. TiMBA differentiates 
three types of roundwood (wood fuel, coniferous and non-coniferous industrial roundwood), two additional raw products for 
paper production (other fibre pulp and waste paper), two intermediate products (mechanical and chemical pulp) and eight finished 
products (coniferous and non-coniferous sawnwoods, veneer sheets and plywood, particle board, fibreboard, newsprint, printing 
and writing paper, and other paper and paperboards). Except for sawnwoods, intermediate and end products are produced from a 
mix of coniferous and non-coniferous industrial roundwood. Scenario simulations with TiMBA are guided by parameters and 
assumptions shaping future developments. In the model framework, wood products are implicitly treated as perfect substitutes, 
regardless of their origin, as long as they belong to the same commodity group. 

As the optimization of the market equilibrium in a given year does not include an elasticity of substitution, consumption 
is merely shifted by changes in income and price (Murray et al. 2004). Thus, the GDP development indicating national incomes 
and is an important driver of change. Since the consumption of wood-based products is positively correlated to income, 
an increase in income basically leads to an increase in demand. The supply of roundwood depends on wood prices and forest 
development which in turn is basically determined by the growth dynamics of forest stock, the change in forest area, and 
harvest volumes. Forest area development and timber supply is coupled to GDP per capita developments based on the concept 
of the environmental Kuznets curve [@Panayotou:1993]. 
[comment]:<> (CM: Someone please add reference for Murray 2004)

In its basic version, TiMBA uses the assumptions made in the “Middle of the road” scenario described in 
“The Shared Socioeconomic Pathways” (the so called SSP2 scenario) to model future GDP developments and population growth. 
This scenario describes a world of modest population growth and where social, economic and technological trends continue 
similarly to historical patterns [@Riahi:2017]. Price and income elasticities of demand are taken from @Morland.2018.
Further exogenous specifications on technology developments (input-output coefficients and manufacturing cost) are estimated
based on historical developments from 1993-2020 while information on trade inertia and cost are based on WTO data as provided
in the Forest Products Model (GFPM, [@Buongiorno:2015]; GFPM version 1-29-2017-World500). 
The base year for the scenario simulations with the current version of TiMBA is 2020. The input data used for simulation 
with TiMBA needs to be calibrated and provided in a source file prior to model runs. This file is provided together with 
the model. The calibration procedure is described in @Buongiorno:2015 and altered according to @Schier:2018. 
The input data for calibrating the model are obtained from three global databases: The FAO forestry statistics (FAOSTAT), 
the FAO Forest Global Resources Assessment (FAO 2020) and the World Bank Development Indicators (World Bank).
[comment]:<> (CM: Wollen wir die Quellen für FAO und Weltbank hier mit angeben oder machen wir das mit Citavi?)

The model output comprises information about production, consumption and trade quantities, and prices as well as forest development. 
The model concept bases on the formal description of GFPM [@Buongiorno:2015;@Buongiorno:2003].

**Table 1:** Modell characteristics

|Model type|Dynamic and static equilibrium market model|
|-----------------------------------| -----------------------------------|
|Geographical scope|Global (180 countries)|
|Temporal Dimension|Recursive long term analyses|
|Products|Raw-, intermediate, end products|
|Data sources|FAO, FRA, WDI, Comtrade|
|Software Implementation|Python 3.12|
|Current code version|TiMBA 1.0.1|
|Permanent link to code repositiory| https://zenodo.org/records/13842492 |
|Code License| APGL3|
|Code versioning system used|GITHUB, Zenodo|
|Optimizer|OSQP|

## Introduction
This paper provides an overview over the data and parameters used in the Timber market Model for policy-Based Analsis 
(TiMBA) and gives an introduction to the model structure and specifications. Further, the results from validating the model 
performance are presented. 

TiMBA is a multi-periodic partial economic equilibrium model for the global forest sector. The model simulates 
production, imports, exports, consumption quantities and prices as well as technological and forest development for 16 
commodities and 180 countries. The prices of wood and wood-based products are endogenous to the model. The market equilibrium 
is subject to market clearance and constraints balancing necessary raw materials and produced wood products and limiting 
the trade [@Samuelson:1952]. In the model framework, wood products are implicitly treated as perfect substitutes, regardless 
of their origin, as long as they belong to the same commodity. As the optimization of the market equilibrium in a given year 
does not include an elasticity of substitution, demand is merely shifted by changes in income and price (Murray et al. 2004).

[comment]:<> (CM: Someone please add reference for Murray 2004)

TiMBA distinguishes between raw, intermediate and end products. The model structure currently includes three types of 
roundwood (wood fuel, coniferous and non-coniferous industrial roundwood), two additional raw products for paper production 
(other fibre pulp and waste paper), two intermediate products (mechanical and chemical pulp) and eight finished products 
(coniferous and non-coniferous sawnwoods, veneer sheets and plywood, particle board, fibreboard, newsprint, printing and 
writing paper, and other paper and paperboards). Commodities and commodity aggregates are determined by the definitions 
of UNECE (2021). Except for sawnwoods, intermediate and end products are produced from a mix of coniferous and non-coniferous 
industrial roundwood. Production of intermediate and end products is modelled using Input-Output coefficients determining 
the level of inputs needed for producing one unit of output. The production level depends on raw material prices, costs of 
manufacturing as well as commodity prices. While the prices of raw materials and intermediate and end-products are simulated 
endogenously, cost of manufacturing and transport are given exogenously. 

[comment]:<> (CM: Someone please add reference for UNECE 2021)

Consumption of wood-based products is tied to country-specific income (GDP) and price levels via price and income elasticities 
taken from @Morland:2018. In TiMBA, demand for wood-based products is positively correlated to income, thus, an 
increase in income basically leads to an increase in demand while demand decreases with increasing product price. 

The supply of roundwood depends on wood prices and stock volume which in turn is determined by the growth dynamics of 
forest stock, the change in forest area, and harvest volumes. TiMBA model import from and to one single country to the 
world. Trade occurs when the price of a product in a certain country exceeds the foreign price plus transport costs or 
vice versa is lower than the world price. Simultaneously, there is a need for trade due to the scarcity of goods in one 
country, which leads in an increased demand or, conversely, an increased supply leading to a surplus in another country. 
This dynamic consequently incentivizes international trade as countries attempt to balance their production and consumption 
through imports and exports. The difference in production costs and prices between countries further reinforce the need 
for such trade interactions in order to optimize resource allocation and market equilibrium. 

Scenario simulations with TiMBA are guided by parameters and assumptions shaping future developments. The GDP development 
indicating national incomes is an important driver of change. In its basic version, TiMBA uses the assumptions made in the 
“Middle of the road” scenario described in “The Shared Socioeconomic Pathways” (the so called SSP2 scenario) to model 
future GDP developments and population growth. This scenario describes a world of modest population growth and where 
social, economic and technological trends continue similarly to historical patterns [@Riahi:2017]. Demand is subject 
to annual changes following the projected GDP growth and endogenous price developments, so that new prices and income levels
shift the demand for wood-based products via elasticities at an annual interval. On the supply side, price and volume elasticities 
shift the wood supply at an annual interval. Forest area development and thus, stock volume and timber supply are coupled 
to GDP per capita developments based on the concept of the environmental Kuznets curve [@Panayotou:1993]. Information on 
trade inertia and cost are based on WTO data as provided in the GFPM ([@Buongiorno:2003]; GFPM-base2021 
https://onedrive.live.com/?authkey=%21AEF7RY7oAPlrDPk&id=93BC28B749A1DFB6%2117056&cid=93BC28B749A1DFB6). The base year 
for the scenario simulations with the current version of TiMBA is 2020. The input data used for simulation with TiMBA 
needs to be calibrated and provided in a source file prior to model runs. This file is provided together with the model. 
The calibration procedure is described in @Buongiorno and Zhu:2015 and altered according to @Schier:2018. The input 
data for calibrating the model are obtained from three global databases: The FAO forestry statistics (FAOSTAT), the FAO 
Forest Global Resources Assessment (FAO 2020) and the World Bank Development Indicators (World Bank). The model output 
comprises information about production, consumption, trade quantities, and prices as well as forest development and 
technology.

The model concept bases on the formal description of the Global Forest Products Model (GFPM) [@Buongiorno:2015;@Buongiorno:2003].

![Caption for example figure.\label{fig:1}](..\images\timba_product_transformation.png)

**Figure 1:** Material flow and product structure in TiMBA. Other fiber pulp and waste paper are solely inputs in the paper sector. 
Wood residues used as input in the wood-based panel and pulp sectors are not explicitly modeled in TiMBA but implicitly considered 
by manufacturing coefficients. Double represent the mix of raw materials as input for further processing. Thus, wood-based panels 
could be made from a single input or a mixture of coniferous and non-coniferous roundwood while paper products could be made from 
a single input or a mixture of pulp and waste paper. The dotted lines indicate that other industrial roundwood is composite product: 
While raw data are imported for data calibration, the amounts of coniferous and non-coniferous other industrial roundwood are 
calculated out from of the total amount of industrial roundwood and summed up as total other industrial roundwood for model simulation. 
The bold lines indicate, that the product is not further processed before sold as end product.

## Model formulation and specifications

TiMBA computes periodical production, import, exports and consumption as well as prices for the forest-based sector considering 
forest resources endowment as well as cost, technology and trade constraints.  The recursive market model consists of a static 
and a dynamic phase. 

In the static phase, TiMBA calculates a global equilibrium across products and countries in a given year. The modelling problem 
is solved for each year by maximizing the economic welfare, defined as the sum of the producer and consumer economic surplus. 

In the dynamic phase, changes in the equilibrium conditions (shifts in parameters determining the model outcome such as growing GDP, 
population or cost) are updated from one period to the next.

The model concept bases on the formal description of the Global Forest Products Model (GFPM) [@Buongiorno:2015;@Buongiorno:2003]. 
The following problem is optimized by using the CVXPY [@Diamond:2016; @Agrawal:2018] package and the OSQP solver [@Stellato:2020]:

$$\max_{Z}=\sum_{i}\sum_{k}\int_{0}^{D_{i,k}}P_{i,k}\left(D_{i,k}\right)dD_{i,k}-\sum_{i}\sum_{k}\int_{0}^{S_{i,k}}P_{i,k}\left(S_{i,k}\right)dS_{i,k}$$
$$-\sum_{i}\sum_{k}\int_{0}^{Y_{i,k}}m_{i,k}\left(Y_{i,k}\right)dY_{i,k}-\sum_{i}\sum_{j}\sum_{k}c_{i,j,k}T_{i,j,k}$$

with $P$ as price, $D$ as demand, $S$ as supply, $Y$ as manufacturing, $m$ as manufacturing costs, $T$ as trade, $c$ as 
transportation costs and the indices $i$ for country, $j$ as trade partner country and $k$ as commodity.

Subject to:
$$S_{i,k}+Y_{i,k}+\sum_{j}I_{j,k}=D_{i,k}+\sum_{n}a_{i,k,n}Y_{i,n}+\sum_{j}X_{j,k}$$

### Demand:

The demand for wood-based products is correlated to income ($y$) and wood prices. 

$$P_{i,k}(D_{i,k}) = P_{i,k,t-1}\left(\frac{D_{i,k}}{D^{*}_{i,j}}\right)^{1/\delta_{i,k}}$$

$$D_{i,k}^{*}=D_{i,k,t-1}\left(1+\alpha_{y}g_{y}+\alpha_{D,t-1}g_{D,t-1}+\alpha_0\right)$$

with $\delta$ as demand price elasticity, $g_y$ as growth rate of income, $g_D$ as exogenous growth rate of demand, $\alpha$ as 
exogenous parameters to shift the influence of the growth rates and t as time index.


### Supply:

The supply of roundwood depends on wood prices and forest development which in turn is basically determined by the growth 
dynamics of forest stock, the change in forest area, and harvest volumes:

$$P_{i,k}(S_{i,k}) = P_{i,k,t-1}\left(\frac{S_{i,k}}{S^{*}_{i,j}}\right)^{1/\lambda_{i,k}}$$

$$S_{i,k}^{*}=S_{i,k,t-1}\left(1+\beta_{y}g_{y}+\beta_{I}g_{I}\right)$$

with $\lambda$ as supply price elasticity, $g_y$ as growth rate of income, $g_I$ as growth rate of forest inventory and $\beta$ 
as exogenous parameters to shift the influence of the growth parameters. Forest area development and thus, timber supply 
is coupled to GDP per capita developments based on the concept of the environmental 
Kuznets curve (Panayotou 2004). See the section 'Forest' for a more detailed description.

[comment]: <> (JT Forest part under section 'Forest' )

### Manufacturing:

$$m_{i,k}(Y_{i,k}) = m^{*}_{i,k,t-1}\left(\frac{Y_{i,k}}{Y_{i,j,t-1}}\right)^{\zeta_{i,k}}$$

$$m^{*}_{i,k}=m_{i,k,t-1}\left(1+g_m\right)$$

with $\zeta$ as manufacturing cost elasticity and $g_m$ as growth rate of manufacturing costs.

### Trade:

$$c_{i,j,k}(T_{i,j,k}) = c^{*}_{i,j,k,t-1}\left(\frac{T_{i,j,k}}{T_{i,j,k,t-1}}\right)^{\tau_{i,j,k}}$$

$$c^{*}_{i,j,k}=c_{i,j,k,t-1}\left(1+g_f+g^i_t+g^x_i\right)$$

with $\tau$ as transportation cost elasticity, $g_f$ as growth rate of freight costs, $g_t^i$ as growth rate of import 
taxes and $g_t^x$ as growth rate of export taxes.

### Forest

The development of forest area is simulated exogenously using the environmental Kuznets curve (EKC) approach [@Kuznets:1955;@Grossmann and Krueger:1991]. 
This concept describes an inverted U-shaped relationship between income development and deforestation. 
Initially, as GDP per capita rises, the rate of deforestation increases until it reaches a turning point. Beyond this 
point, further increases in GDP per capita result in a decreasing rate of deforestation [@Panayotou:1993]. Forest stock growth 
is linked to the development of the area.

[comment]: <> (Panayotou 2004 als Bibtext Referenz in .bib )

$$g_{I}=\left(1+\gamma_0\left(\frac{I_{t-1}}{A_{t-1}}\right)^\sigma+\left(\alpha_0+\alpha_{1}y^{'}\right)e^{\alpha_{2}y^{'}}\right)$$

with $I$ as forest inventory, $A$ as forest area, $\sigma$ as elasticity of inventory per unit area, $y^{'}$  as per capita 
income and $\gamma$ and $\alpha$ as exogenous parameters to shift the growth rates.

Forest stock evolves over time to a growth-drain equation following @Buongiorno:2015:

$$I_t=\left(I_{-1}+(g_a+g_u+g_u^*)I_{-1}\right)-pS_{-1}$$

where g_a is annual rate of change of forest area, g_u is periodic rate of forest growth, 
g_u^* is the adjustment rate of forest growth and $pS_{-1}$ is harvest of previous period .

All necessary data is provided in the supplied input file. The CO2 price cannot be adjusted in the base version of TiMBA. 
A separate extension will be provided for this purpose. 

[comment]: <> (JTCopied forest formula from supply part)

## Countries and Products
For each of the 180 countries considered in the model, TiMBA includes three main sectors along the forest-based value chain: 
the forestry sector, the wood-processing based industries and the consumers of forest-based products. The forestry sector 
provides the forest resources to supply fuelwood as well as coniferous, non-coniferous and other industrial roundwood. 
Forest industries then transform coniferous and non-coniferous industrial roundwood into intermediate and end products 
which are either used as input for, e.g., paper production or demanded by consumer markets. 

Beyond four types of roundwood, the product structure in TiMBA further distinguishes coniferous and non-coniferous sawnwood, 
plywood and veneer sheets, particle board including OSB, fibre board, newsprint, printing and writing paper and other paper 
and paper board as end products as well as mechanical and chemical pulp (including semi-chemical pulp) as intermediate and 
other fibre pulps and waste paper as additional raw materials. For these products TiMBA simulates the production, import, 
export, consumption and prices for each year and country. As shown in table x, not every product is subject to trade, 
manufacturing or consumer demand. 

## Input Data and Parameter

TiMBA uses input data and parameter from various sources. Input data for TiMBA are subject to a goal-programming based 
calibration procedure tackling data inconsistencies and determining initial input-output coefficients as well as manufacturing 
cost along the wood-based value adding chain. The model calibration for TiMBA follows the procedure as formally described in
@Buongiorno:2015 and modified by @Schier:2018. Currently, the calibration procedure is not included int the TiMBA 
package. The calibrated data are provided in form of an Excel sheet as input for simulations together with the model under 
https://github.com/TI-Forest-Sector-Modelling/TiMBA

### Overview on Input Data 
[comment]: <> (JT"Product consumption for the base year is then calculated as production + imports – exports" and manufacture?)
Data on country-specific production and trade volumes of raw, intermediate, and end products are taken from FAOSTAT. 
Product consumption for the base year is then calculated as production + imports – exports. Further, data on country-specific 
export values are used to compute the unit product prices in the base year as the total export volume divided by total 
export quantity stated in constant US $ of 2018 using the GDP deflator from the World Development Indicators database 
(Code NY.GDP.DEFL.ZS). Unit prices differ for net-importer and net-exporter countries. The unit price of net-importers 
of a given commodity is the export unit price plus commodity specific freight costs and tariffs. 

Data on GDP and population are derived from the World Development database (Worldbank xxx) under the indicator names 
"GDP (current US$)" and "Population, total" specified by the codes NY.GDP.MKTP.CD and SP.POP.TOTL, respectively. 

Tariffs are derived from WTO Integrated Database (IDB) notifications as average of ad valorem duties for the last current 
year available of the respective reporter country and product on HS-code level 4 – 6. Freight cost are calculated as 
freight factor times export unit value. Freight factors are taken from the Forest Sector Model GFPM [@Buongiorno:2003] (see Table A1), 
GFPM-base2021 (https://onedrive.live.com/?authkey=%21AEF7RY7oAPlrDPk&id=93BC28B749A1DFB6%2117056&cid=93BC28B749A1DFB6) 


Data on national Forest Area and Growing Stock on Total Forest Area (in the following Forest Stock) are taken from the 
FAO Forest Resources Assessment 2020. In case that data on Forest Stock had not been reported in 2020, data were complemented 
by the authors either by (i) searching for the last available record on Forest Area, (ii) using data on growing stock on 
naturally regenerated and/or planted forest area or (iii) calculate the Forest Stock from biomass stock data. If none of 
these information were given, the authors use the entries on living woody biomass density from GlobalForestWatch2000 to 
derive the Forest Stock of a given country. When the national forest area was reported to be > 1, growing stock on total 
forest area was required to be at least  1. 
 

### Overview on Parameters 

Wood products consumption is tied to the product price and income (GDP). These relations are represented by elasticities 
of demand. Wood production is driven by prices of raw materials as well as the forest stock density of a country and 
represented by respective elasticities. It is assumed that wood supply equals wood removals from the forest. Supply of 
wastepaper and other fibre pulp depends on product prices and national income (GDP). All elasticities are summarized in 
table xx.

Manufacturing of intermediate and end products is determined using country and product-specific input-output coefficients 
and manufacturing cost. Manufacturing cost of each product represent all cost of inputs not explicitly modeled in TiMBA 
(labor, energy, capital, additional materials) excluding cost of raw materials in a given year and country. The input-output 
coefficient of each product in a year and country states the amount of input going into one output. These parameters are 
determined for each country and product during the model calibration (see above) and depend on production and trade data 
from FAOSTAT and fixed bounds on minimum and maximum input per output and cost. 

Forest stock growth without harvest is negatively correlated to forest density as described by the elasticity of -0.45 
[@Buongiorno:2015].  Via an environmental Kuznets curve the rate of forest area change is linked to the GDP per capita. 
The effects of GDP per capita and squared GDP per capita on the forest area annual growth rates are again taken from 
@Buongiorno:2015 who estimated the coefficients to be 0.0014 and 0.0898 (see equation xx), respectively. 
The ratio of wood drain from the forest to harvest is set to be 1.2 expressing that 20% of the above ground biomass is 
left after harvesting as logging residues while 80% is supplied as roundwood. 

For lack of data, some of the parameters had to be set intuitively, based mostly on the dynamic behavior of the model.

**Table 2:** Items simulated with TiMBA. Product definitions according to FAOSTAT and FAO Forest resources assessment (Quellen) 

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
**Figure 2:** Countries which are included in TiMBA


**Table 4:** Demand and supply elasticities

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
| Wastepaper              |          |          | 1.0000   | 0.6700   | \-      |
| Other Fibre Pulp        |          |          | 1.0000   | 0.1400   | \-      |

Note: This is a summarizing table; Elasticities are shown for the best model, which is chosen on the basis of Breusch-Pagan, Maddala-Wu and Hausman tests based on @Morland:2018 taken from GFPM [@Buongiorno:2003], GFPM-base2021 (https://onedrive.live.com/?authkey=%21AEF7RY7oAPlrDPk&id=93BC28B749A1DFB6%2117056&cid=93BC28B749A1DFB6) 

### Exogenous Parameter Development

Currently, TiMBA simulates forests and wood product market developments until 2050. Beyond the endogenous equilibrium process, exogenous parameters shift the development pathway form year to year including parameters on country-specific GDP and population growth as well as on as growth rates for country- and product specific input-output ratios and manufacturing costs. 

Data GDP and population growth are taken from the “Middle of the road” scenario (SSP 2) described in “The Shared Socioeconomic Pathways” as provided by IIASA data base (QUELLE). Parameters driving forest growth others than GDP per capita are held constant. Future development of input-output coefficients and manufacturing cost were estimated by the authors in a subsequent study based on historical data. Trade activities are contraint by constant trade internia bounds as defined in the GFPM (Buongiorno et al. 2003), GFPM-base2021 (https://onedrive.live.com/?authkey=%21AEF7RY7oAPlrDPk&id=93BC28B749A1DFB6%2117056&cid=93BC28B749A1DFB6). 

## Computer software

### General description and software installation
TiMBA is an open-source, ready-to-use model for the global forest sector written in Python, complying with modern programming
standards (PEP8). The model is hosted and distributed using [GitHub](#https://github.com/TI-Forest-Sector-Modelling/TiMBA).
The versioning is managed using [Zenodo](#https://zenodo.org/records/13842492). TiMBA relies exclusively on open-access and
free-of-charge packages, which allow users to conduct analyses without higher software costs. In that way, TiMBA tries to
encourage transparent and community-based forest sector analyses. 

The model has a modular structure that allows the adaptation of the model to the targeted research question by turning 
off or on independent functionalities. Further, this structure enables users to extend the model framework with new features 
by adding new modules while limiting possible damage to other model components.   

In TiMBA, demand, supply, import, export, and manufacture are handled as domains with separate specificities.
As a recursive PE model, TiMBA has a static and a dynamic phase for each period. In the static phase, functions for each
domain described above are linearized based on input data for the base period and on optimization results and parameter
shifts for all other periods. In the dynamic phase, key parameters of the model are shifted to reflect scenario
assumptions on socioeconomic, environmental, and technological changes. Details on parameter shifts in each domain are 
provided in the [model formulation](#model-formulation-and-specifications).
The linearized domain functions are vectorized and bundled in the quadratic objective function. The economic equilibrium 
in a given period is calculated by using a quadratic solver OSQP [@Stellato:2020] embedded in the environment [CVXPY](https://www.cvxpy.org/version/1.1/index.html) 
[@Diamond:2016; @Agrawal:2018]. The CVXPY environment offers a large range of settings and other quadratic solvers. 
However, only the model results calculated with default solver settings delivered with TiMBA were exhaustively tested. 
All changes in the solver environment or the solver settings might impact the results.    


#### Installing TiMBA
To download and install TiMBA on your local device, following steps are required:

1. Clone the repository: <br>
Begin by cloning the repository to your local machine using the following command: 
    >git clone https://github.com/TI-Forest-Sector-Modelling/TiMBA.git
    > 
2. Switch to the TiMBA directory:  
Navigate into the TiMBA project folder on your local machine.
   >cd TiMBA
   >
3. Create a virtual environment:  
It is recommended to set up a virtual environment for TiMBA to manage dependencies. The package is tested using 
   Python >3.9 (3.9 and 3.12). We can not guarantee the full functionality of the package with another Python version.
   Select the correct Python interpreter.   
   Show installed versions: 
   >py -0  
   >
   - If you have installed multiple versions of Python, activate the correct version using the py-Launcher.
   >py -3.8 -m venv venv 
   > 
   - If you are using only a single version of Python on your computer:
   >python -m venv venv
   >
4. Activate the virtual environment  
Enable the virtual environment to isolate TiMBA dependencies. 
   >venv\Scripts\activate
   >
5. Install TiMBA in the editable mode  
   >pip install -e .

If the following error occurs: "ERROR: File "setup.py" or "setup.cfg" not found."
you might need to update the pip version you use with: 
>python.exe -m pip install --upgrade pip

#### Check installation

To check if the installation was successful, the following command can be run from the terminal:  
   >run_timba --help

The help provides you with information about the basic model settings, which can be changed to adapt model runs to your
needs(see section [Model settings](#model-settings) for further details).

Test if TiMBA is running by executing the model only for the first period:

  >run_timba -MP=1


The TiMBA model comes with a test suite to ensure its functionality while allowing for continuous integration and development of new features. 
Run the test suite to check the functionality of the package and validate the produced results with those provided by the
TI-FSM using the coverage report:

  > coverage run


To reduce the test suite running time, only the first period will be computed and compared. The test suite results will not be saved.
The computed results and provided validation results are compared with a relative tolerance of 5%.  

The coverage report of the TiMBA model can be accessed using:
 > coverage report


### Model settings
Users can interact with TiMBA in multiple ways. When running TiMBA from a terminal (e.g., CMD), the integrated [CLI](#settings-as-parameters) 
allows users to change basic model parameters and turn on or off specific modules. More [advanced settings](#advanced-settings) can be 
accessed in `default_parameter.py`. Changes in settings made via the CLI will overwrite parameters in `default_parameters.py`

Multiple settings are integrated in TiMBA to allow users to interact with the model and adapt the modelling parameters to their research interests.
The following chapter provides a brief overview of the model settings.  

Basic model settings include:

- The flag `default_year` controls the base year of simulation [`default: 2020`]: The integer defines the year in which the simulation starts. If the user-defined base
year does not correspond to the base year in the entries in `scenario_input.xlsx`, TiMBA corrects automatically user-defined settings.


- The flag `default_max_period` controls the maximum number of periods for the simulation [`default: 10`]: The maximum number of periods determines how many periods
TiMBA will calculate. Depending on the structure of `scenario_input.xlsx`, the end year might vary. TiMBA calculates until 2050 with the default settings and input data. 


- The flag `default_calc_product_price` controls how product prices in TiMBA are obtained [`default: shadow_PP`]: The model comes with two options. While
prices obtained using both ways can be identical, differences for specific countries and products are common.
  - If `shadow_PP` is selected, shadow prices (dual values) directly obtained from the optimization are used as product prices. This is the default option in the model.
  - If `calculated_PP` is selected, product prices are calculated based on optimized quantities using price elasticities.


- The flag `default_calc_world_price` controls how world market prices in TiMBA are obtained [`default: shadow_WP`]: 
The model comes with three options, which can lead to significant differences in the projections. Only the option
`shadow_WP` has been validated extensively.
  - If `shadow_WP` is selected, world market prices are directly obtained from the optimization (dual values). This is the default option in the model.
  - If `constant_WP` is selected, world market prices are held constant on the level of the base year.
  - If `average_WP` is selected, world market prices are calculated as the weighted average of product prices in all countries


- The flag `default_MB` controls the form of the material balance, which is handed over to the solver [`default: C_specific_MB`]: 
The model comes with three options, which impact the total number of optimization constraints and, thereby, the model's runtime.
The optimization results can vary depending on the selected material balance option. Only the default option has been validated extensively.
  - If `C_specific_MB` is selected, the material balance is formulated as a commodity-specific optimization constraint,
  which is applied for all countries. In this case, the number of optimization constraints related to the material balance
  equals the number of modelled commodities.
  - If `RC_specific_MB` is selected, the material balance is formulated as a commodity-specific and country-specific 
  optimization constraint. In this case, the number of optimization constraints related to the material balance
  equals the number of modelled commodities times the number of countries.
  - If `RCG_specific_MB` is selected, the material balance is formulated as a country-specific optimization constraint 
  for different commodity groups (raw, intermediate, and final products, as well as fuelwood and other industrial roundwood).
  In this case, the number of optimization constraints related to the material balance equals the number of commodity groups
  times the number of countries.


- The flag `global_material_balance` activates the global material balance, balancing all wood flows globally using the
buffer region zy [`default: False`].


- The flag `serialization_flag` controls if serialized input pkl files are used instead of provided input xlsx files
[`default: False`]. This flag allows to accelerate the data processing steps which process and save the input xlsx files
into the data containers. If new input xlsx files are used, we recommend deactivating the flag to pass over changed
inputs to TiMBA. New input xlsx files will automatically be serialized after the processing. After the update of serialized 
files, the activation of the serialization flag is recommended when to speed up sensitivity analyses with unchanged input files.    


- The flag `dynamization_activated` controls if key parameters of TiMBA are dynamized according to defined shifts in the
sheet ExogChange in `scenario_input.xlsx` to reflect socioeconomic, environmental, and technological changes (see
[exogenous parameter development](#exogenous-parameter-development) for details) [`default: True`]   


- The flag `constants` controls if the slope and intercept of linearized domain functions and product prices are constant
over the simulation timeframe. The list of boolean allows controlling the variability of all three components separately
where the following position corresponds to the following element: [constant prices, constant slopes, constant interceps].
We recommend using the `default: [False, False, False]` which has been validated exhaustively. Changed combinations can
have a significant impact on the model results or even lead to optimization unfeasibility.


- The flag `capped_prices` controls if product prices obtained from the optimization or calculated are capped to avoid
price outliers [`default: False`].


- The flag `cleaned_opt_quantity` controls if optimized quantities are cleaned using upper and lower bounds aligned with 
exogenous entries to avoid quantity outliners [`default: False`].


- The flag `verbose_optimization_logger` controls if information outputs related to the optimization steps are printed 
in the console and logged [`default: True`].


- The flag `verbose_calculation_logger` controls if information outputs related to all modelling steps apart from the 
optimization are printed in the console and logged [`default: False`]. 


- The flag `read_additional_information_file` controls if the additional input files from the folder 
02_Additional_Information are processed. The additional information holds important data for additional modules 
[`default: True`] 


- The flag `test_timba_results` controls if produced model results are tested against a set of validation results (ground
truth results) [`default: True`]. This flag is relevant for the test suite of TiMBA which allows us to exhaustively check
the functionality of the model after code changes. The test suite is triggered when a working branch is pulled into the
main branch.    


- The flag `default_transportation_impexp_factor` controls a factor for Transportation Import/Export [`default: 1`].

[comment]: <> (Weiß jemand noch weiß was diese Flag nochmal bewirkt? Ich habe ein bisschen gesucht aber konnte die Stelle der Verwendung nicht ad-hoc finden)

As described, TiMBA is delivered with a set of default settings, which were tested and validated. For standard usage, we 
recommend to use default parameters. For more advanced usage and model development, changes in default parameters might
be necessary.

  
#### Settings as parameters
The CLI provides to access basic model settings, and their default values (see [basic model settings](#model-settings)). 
Check if the CLI command is registered and available on your computer by executing either:

- >run_timba --help

Default settings can be changed in the following way:
- > run_timba -MP=5 -PP="calculated_PP" -WP="shadow_WP"

For this example, TiMBA will simulate 5 periods using calculated prices as product prices and shadow prices as world market prices.

#### Advanced settings
In addition to the settings accessible via the CLI or `default_parameters.py`, users can control advanced settings through
changes in `Defines.py`. Advance settings include:

- Solver settings (detailed descriptions can be accessed in the [CVXPY documentation](https://www.cvxpy.org/version/1.1/index.html))
  - The variable `MAX_ITERATION` defines the maximal amount of iteration for the solver to solve the optimization problem [`default: 500000`].
  - The variable `REL_ACCURACY` defines the relative accuracy of the solver when solving the optimization problem while
  accounting for the optimization constraints [`default: 0.00025`].
  - The variable `ABS_ACCURACY` defines the absolute accuracy of the solver when solving the optimization problem while
  accounting for the optimization constraints [`default: 0.00001`].

By modifying the solver settings, the user can change the optimization's runtime giving more or less flexibility to the solver.
Modifications in the solver settings are likely to impact the model results and should therefore be followed by a result
validation.  

- Optimization settings:
  - The variable `TRADE_INERTIA_DEVIATION` defines relative deviations allowed from set trade inertia bounds for all
  countries, which gives additional flexibility to trade [`default: 0.005`]. 
  - The variable `TRADE_INERTIA_DEVIATION_ZY` defines relative deviations allowed from set trade inertia bounds for the
  buffer region zy, which gives additional flexibility to absorb global export surpluses and compensate for global import 
  deficits [`default: 0.001`].
  - The variable `TRADE_BOUND_DEVIATION_PENALTY` defines the penalty applied in the optimization for deviations from 
  trade inertia bounds, which gives additional flexibility to the solver [`default: 99999999`]. 
  - The variable `TRADE_PREV_DEVIATION_PENALTY` defines the penalty applied in the optimization for deviations from traded
  quantities in the previous period, which gives additional flexibility to the solver [`default: 0`]
  - The variable `PRICE_DEVIATION_THRESHOLD` defines the relative threshold for allowed price changes compared to prices 
  from the previous period [`default: 0.5`]. The threshold is activated when the flag `capped_prices` is turned on. 

All optimization settings related to trade allows to provide additional flexibility to the solver regarding the trade.
The settings can be changed to 0 to deactivate the flexibility mechanism. Default settings are calibrated to the most accurate 
trade and world market prices.


**Disclaimer**:
The model was validated for a selection of settings. Some setting combinations might not be coherent and can lead to
unfeasibility problems, simulation errors or unreliable results. Without any further specification, TiMBA
will use default settings.
Users can adapt the input file (scenario_input.xlsx) to conduct more complex scenario-based analyses.
Changes in the sheet "ExogChange" allow the user to shift exogenously model parameters to reflect
socioeconomic, environmental and technological changes. Some parameter developments might be not coherent or compatible
with the model's theoretical framework resulting in unfeasibility problems or unreliable results. In case of problems,
users should double-check the consistency of changes made in the input files.

### Data handeling and processing
All input data required to run TiMBA in its basic version are provided in the project (`scenario_input.xlsx`). All input
data are processed and stored in multiple data containers, which are serialized and saved in the folder 03_Serialization.
By activating the flag `serialization_flag`, processing steps will be skipped and a serialized data container will be used 
instead.
TiMBA allows users to provide multiple input files to the model by adding them to the corresponding folder. TiMBA will 
automatically loop over all provided files.

```bash
.
`- data
  `-- input
    `-- 01_Input_Files
      |-- scenario_input.xlsx # contains all input data for the model. 
    `-- 02_Additional_Informations
      |-- additional_information.xlsx 
      |-- worldprice.xlsx
    `-- 03_Serialization
      |-- AddInfoContent.pkl # contains serialized information about the last input data which is processed by the model
      |-- WorldDataContent.pkl # contains serialized information about the last input data which is processed by the model
      |-- WorldPriceContent.pkl # contains serialized information about the last input data which is processed by the model
```

The package will generate a result directory called `output` which is located inside the data folder. The final directory
after one run will look something like this:

```bash
.
`- data
  `-- output
      |-- ....log # contains the logged process of the simulation
      |-- DataContainer_....pkl # contains all output information as pkl file
      |-- results....csv # contains main results as csv file
      |-- worldprices....csv # contains world price results as csv file
      |-- forest....csv # contains forest area and stock results as csv file
      |-- manufacture....csv # contains results for manufacturing as csv 
      |-- results_aggregated....csv # contains aggregated results on continent level as csv file

```
**Important output information**  
No output file will ever be overwritten by the application itself. New results files will be generated in the format
`results_D<yyyymmdd>T<hh-mm-ss>.csv` and will be saved to the output folder as well. The log file itself won't be overwritten
as well but also no new file created on additional runs. Log information gets appended to the existing log file.
Removing the log file ahead of executing the model won't result in errors.

To handle and process data TiMBA relies on packages such as pandas and numpy. While running TiMBA stores all data into
the data container for each domain separately (see exemplary structure overview). There, data is saved in pandas data frames.
This allows to access all data at any point of processing. Original data from the input files are stored as `data`.
The data of all domains are harmonized to a uniform length to facilitate the handling in the optimization 
(called `data_aligned`). `data_aligned` always only holds the data of the current period.

In preparation for the optimization, data of all relevant domains are vectorized in one separate data container 
`OptimizationHelpers`. The optimization results are stored in the respective domains and merged in `OptimizationResults`,
which holds all additional information used by the solver. 

```bash
.
`- self
  `-- Data # Overarching data container 
      |-- Demand # contains data related to demand
          |-- data  # contains original data from scenario_input.xlsx
          |-- data_aligned # contains harmonized data of the current period
          |-- data_periods # contains harmonized data with optimization results of all calculated periods so far
          |-- domain  # domain name
          |-- file path # path of the input file
      |-- ExogChangeDemand # contains data related to exogenous shifts for demand
          |-- data  # contains original data from the input files
          |-- data_aligned # contains harmonized data
      ...
      |-- Other domains 
      ...
      |-- OptimizationHelpers  # contains vectorized data 
          |--data # contains vectorized data of the current period
          |--data_periods # contains all vectorized data of all calculated periods so far

```

### TiMBA workflow and development roadmap

TiMBA is embedded in a larger workflow, which allows for conducting global scenario-based analyses in a semi-automated way. 
Besides the main application TiMBA, this workflow is composed of supportive packages to calibrate data from multiple sources and automatically
generate input files tailored to specific research questions. Users can dynamically explore and analyze the optimization
results. The supportive packages are planned to be published in future extensions of TiMBA.

Further, diverse plugin extensions of TiMBA are currently under preparation at the Thünen Institute of Forestry, which
will expand the model's capacities or refine aspects of the basic model version. All extensions are planned to be
integrated into TiMBA's basic version.
Collaborative efforts with external experts to advance TiMBA's basic version or develop new plugin extensions will be 
fostered.

A continuous upgrade of TiMBA to newer Python and package versions is planned but will depend on available time
capacities within the TiMBA team.


[comment]: <> (Lehnen wir hier mit der Beschreibung zu weit aus dem Fenster? Sollten wir das erstmal für uns behalten?)

![TiMBA_software_workflow](..\images\TiMBA_planned_workflow.png)
**Figure 3:** Software workflow of TiMBA, including supportive packages and extensions

### Software requirements
TiMBA was developed and tested using a Windows operating system (Windows 10 Enterprise) with 32 GB RAM and Python 3.9.  
The compatibility with other operating systems (Ubuntu and MacOS) is continuously tested via GitHub Actions. Operating
systems with lower computational capacities might encounter problems when running TiMBA.

All necessary packages to run TiMBA are automatically installed when downloading the project from GitHub and activating
the virtual environment. Step-by-step instructions about the installation procedure are provided in the README.md. All
packages integrated into TiMBA, including the solver, are open-access and free of charge. 

[comment]: <> (Ich habe diesen Teil mit den Information von meinem Computer geschrieben. Vielleicht könntet ihr mal
 schauen, ob das auch mit euren Betriebssystemseigenschaften übereinstimmt)
[comment]: <> (Bitte die ersten Sätze richtig ergänzen)



## Validation
[comment]: <> (CM: Satz zur Validierung)
TiMBA was subject of an extensive validation process which was designed to assure the quality and functionality of the model. More information about the valiation process and results will be published seperatly and following soon.


### Projection / historic data replication


### Inter-model comparison


### Economic shocks / economic behaviour 


## Annex

**Table A1:** Freight cost of shipping one unit of commodity from origin to destination

|Commodity|Freight Cost|
|:--------|:----------:|
|IndRoundNC|	32|
|SawnwoodNC|	50|
|Fuelwood|	14|
|IndRound|	17|
|OthIndRound||	
|Sawnwood|	23|
|Plywood|	22|
|ParticleB|	10|
|FiberB|	15|
|MechPlp|	37|
|ChemPlp|	44|
|OthFbrPlp|	109|
|WastePaper|	33|
|Newsprint|	28|
|PWPaper|	52|
|OthPaper|	55|
|  ||
|IndRoundNC|	37|
|IndRound	|20|
|Newsprint|	22|

**Table A2:** List of 180 countries included into forest sector modelling

|Africa|	Asia|	Europe|	North America|	Oceania|	South America|
|:---:|:---:|:---:|:---:|:---:|:---:|
|AGO|	AFG|	ALB|	ANT|	AUS	|ARG|
|BDI|	ARE|	AUT|	BHS|	COK|	BOL|
|BEN|	BGD|	BEL|	BLZ|	FJI|	BRA|
|BFA|	BHR|	BGR|	BRB|	NCL|	CHL|
|BWA|	BRN|	BIH|	CAN|	NZL|	COL|
|CAF|	BTN|	CHE|	CRI|	PNG|	ECU|
|CIV|	CHN|	CZE|	CUB|	PYF|	GUF|
|CMR|	CYP|	DEU|	DMA|	SLB|	GUY|
|COD|	IDN|	DNK|	DOM|	TON|	PER|
|COG|	IND|	ESP|	GTM|	VUT|	PRY|
|CPV|	IRN|	FIN|	HND|	WSM|	SUR|
|DJI|	IRQ|	FRA|	HTI|		URY|
|DZA|	ISR|	GBR|	JAM|		VEN|
|EGY|	JOR|	GRC|	LCA||		
|ETH|	JPN|	HRV|	MEX||		
|GAB|	KHM|	HUN|	MTQ||		
|GHA|	KOR|	IRL|	NIC||		
|GIN|	KWT|	ITA|	PAN||		
|GMB|	LAO|	LUX|	SLV||		
|GNB|	LBN|	MKD|	TTO	||	
|GNQ|	LKA|	MNE|	USA||		
|KEN|	MDV|	NLD|	VCT||		
|LBR|	MMR|	NOR|||			
|LBY|	MNG|	POL|||			
|LSO|	MYS|	PRT|||			
|MAR|	NPL|	ROU|||			
|MDG|	OMN|	SRB|||			
|MLI|	PAK|	SVK|||			
|MOZ|	PHL|	SVN|||			
|MRT|	PRK|	SWE|||			
|MUS|	QAT||||				
|MWI|	SAU||||				
|NER|	SGP||||				
|NGA|	SYR||||				
|REU|	THA||||
|RWA|	TLS||||				
|SDN|	TUR||||				
|SEN|	VNM||||				
|SLE|	YEM||||			
|SOM|||||					
|STP|||||					
|SWZ|||||					
|TCD|||||					
|TGO|||||					
|TUN|||||				
|TZA|||||					
|UGA|||||				
|ZAF|||||					
|ZMB|||||			
|ZWE|||||					

<br><br>

**Table A2:** List of 180 countries included into forest sector modelling
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


### Parameter list

**Table A3:** List of paramter for model input

|Forest        |Supply     	  |Transportation        |Demand |Manufacturing|
|:-------------|:-------------|:-------------|:-------------|:-------------|
|gdp_per_capita_base_period|	price|	freight_cost|	price|	net_manufacturing_cost|
|forest_stock|	quantity|	import_ad_valorem_tax_rate|	quantity|	quantity|
|growth_rate_forest_stock|	elasticity_price|	export_ad_valorem_tax_rate|	elasticity_price|	elasticity_price|
|elasticity_growth_rate_forest_stock|	elasticity_gdp|	quantity|	elasticity_gdp|	
|forest_area|	elasticity_stock|	elasticity_trade_exporter|	elasticity_expectations||	
|forest_area_growth_rate|	elasticity_area|	elasticity_trade_importer|	lower_bound||	
|linear_gdp_forest_area_growth_rate|	elasticity_fourth|	trade_inertia_bounds|	upper_bound||	
|exponential_gdp_forest_area_growth_rate|	elasticity_fifth|	price|||		
|fraction_fuelwood|	elasticity_sixth|	elasticity_price|||		
|ratio_inventory_drain|	elasticity_respect_previous_period_supply|			
|max_ratio_inventory_drain|	lower_bound|			
|CO2_growing_stock|	upper_bound||||			
|price_CO2|	last_period_quantity||||			
|alpha||||||				
|gamma||||||				
|periodic_growth_rate_of_forest_area|||||				
|forest_growth_without_harvest|||||				
|supply_from_forest|||||				

<br><br>

**Table A4:** List of parameter for dynamic changes over time

|Forest        |Supply     	  |Transportation        |Demand |Manufacturing|
|:-------------|:-------------|:-------------|:-------------|:-------------|
|growth_rate_stock|	elasticity_price|	change_freight_cost|	elasticity_price|	growth_rate_net_manufacture_cost|
|growth_rate_area|	growth_rate_value|	change_import_tax_rate|	growth_rate_value|	change_input_output|
|growth_rate_gdp|	growth_rate_gdp|	change_export_tax_rate|	growth_rate_gdp||	
|adjustment_endogenous_growth_rate_stock|	elasticity_gdp|	exogenous_growth_rate_export_trade_shift|	growth_demand_expected|	|
|elasticity_growth_rate_stock_on_area|	growth_rate_fourth_shift|	elasticity_trade_exporter_shift	|growth_lower_bound	||
|growth_rate_linear_GDP_forest_area_growth_rate|	growth_rate_fifth_shift|	exogenous_growth_rate_import_trade_shift	|elasticity_gdp|	|
|growth_rate_squared_GDP_forest_area_growth_rate|	growth_rate_sixth_shift|	elasticity_trade_importer_shift|||		
|fraction_fuelwood|	growth_rate_upper_bound|	trade_inertia_bounds|||		
|ratio_inventory_drain||||||				
|max_ratio_inventory_drain|||||				
|price_CO2|||||				
	
