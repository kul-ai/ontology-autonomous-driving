# An ontology of autonomous driving based on the SAE J3016 standard

[SAE J3016 - Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles](https://www.sae.org/standards/content/j3016_202104/)


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
