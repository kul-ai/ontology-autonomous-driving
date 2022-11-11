# An ontology of autonomous driving based on the SAE J3016 standard

## SAE J3016
[SAE J3016 - Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles](https://www.sae.org/standards/content/j3016_202104/)

## BFO 2022

An ontology of autonomous driving is complient with [BFO 2022 (ISO/IEC 21838-2:2021)](https://basic-formal-ontology.org/bfo-2020.html).

## Contributing 
Before creating a pull request:

1. Check hygiene...

Being in the serializer_and_hygiene folder run

```
python hygiene.py -i "../../ontology-autonomous-driving" -t "hygiene"
```

The hygiene testing is based on ontology testing procedure worked out by the [FIBO community](https://github.com/edmcouncil/fibo).

2. Serialize all TTL files. 

Being in the serializer_and_hygiene folder run

```
python serialize.py -t "../../ontology-autonomous-driving"
```

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Acknowledgements

The research was supported by the [National Science Centre](https://www.ncn.gov.pl/en), Poland (HARMONIA, UMO-2017/26/M/HS1/01092). The project's principal investigator was Piotr Kulicki (KUL, Lublin).

We are grateful to Barry Smith and the BFO team for the opportunity to discuss the ways in which our ontology was based on the BFO. A dedicated seminar took place in Buffalo on April 2022.

We want to also thank to the [Automotive Ontology Working Group](https://www.w3.org/community/gao/) for reviewing the first version of our ontology for AV. 
