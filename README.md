# Langgregate
A simple tool to turn aggregate lang files into lang files under seperate namespaces

This tool assumes all lang entries follow the `x.namespace.etc` format. If a lang entry follows `namespace.x.etc`, it will not work correctly.
## Usage
In a new python file:  
`import langCreate from langgregate`\
(Semi-optional, everything can be done in the central file)

Enter your aggregate lang file as a new dictionary, and use\
`langCreate(lang, language)`\
where `lang` is your aggregate lang file, and `language` is the language code you want to create the lang files for, such as `en_us` or `de_de`. 
