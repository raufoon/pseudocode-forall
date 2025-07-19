
## Pseudocode-forAll 
- *Pseudocode-forAll* executes pseudocode following the CAIE Pseudocode Guide, applicable for exams on 2025-2029. This project is provided for personal, non-commercial use only.
- For the smoothest coding experience, turn off syntax check by selecting **Tools>Settings>Editor>[scroll down] Code Diagnostics>None**.
- Use the magic command syntax: `%%pseudocode` or `%%pseudocode <filename>.pseudo` at the top of the cell with your code in the rest of the cell as shown in the following examples.
- Pseudocode-forAll works by using python to translate your pseudocode to Pascal/Delphi, which is compiled and executed.
- If you suspect there are issues with the pseudocode translator, open an [issue](https://github.com/raufoon/pseudocode-forall/issues) or ask a question in the [discussions](https://github.com/raufoon/pseudocode-forall/discussions) on GitHub including code that reproduces the issue.
- You can also contribute to the [wiki](https://github.com/raufoon/pseudocode-forall/wiki).
- To improve the display of the assignment operator `<-`, use the [Colab Arrow Assignment Operator with Fira Font](https://greasyfork.org/en/scripts/542951-colab-arrow-assignment-operator-with-fira-font) userscript with Tampermonkey. This formats `<-` as a left arrow (←) with a ligature using the Unicode character.

## How to set up in Google Colab

Run the following commands in a code cell to clone the repository and run the setup script:

```python
!git clone https://github.com/raufoon/pseudocode-forall
%run pseudocode-forall/setup.py
````

After that, you can run pseudocode directly in a cell using the `%%pseudocode` magic, for example:

```pseudocode
%%pseudocode
OUTPUT "Hello, world!"
```

## Supported Features

### Formatting and Structure

* Monospaced font, consistent case (uppercase keywords, camelCase identifiers)
* 3-space indentation, comments with `//`
* Optional line numbering

### Variables, Constants, Data Types

* Basic types: `INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN`, `DATE`
* Variable and constant declarations (`DECLARE`, `CONSTANT`)
* Assignment using `←`
* Literal handling (including empty strings and dates)

### Arrays

* One-dimensional and two-dimensional fixed-length arrays
* Explicit lower and upper bounds
* Element access and array-level assignments

### User-defined Data Types

* Enumerated types
* Pointer types
* Composite types: `RECORD`, `SET`, `CLASS/OBJECT`

### Common Operations

* Input: `INPUT`
* Output: `OUTPUT`
* Arithmetic: `+`, `-`, `*`, `/`, `DIV`, `MOD`
* Relational: `=`, `<>`, `<`, `<=`, `>`, `>=`
* Logic: `AND`, `OR`, `NOT`
* String functions: `RIGHT`, `LENGTH`, `MID`, `LCASE`, `UCASE`, concatenation `&`
* Numeric functions: `INT`, `RAND`

### Selection

* `IF ... THEN ... ELSE ... ENDIF` (including nested IF)
* `CASE OF ... ENDCASE` with `OTHERWISE` and range cases

### Iteration (Repetition)

* Count-controlled loops: `FOR ... TO ... [STEP] ... NEXT`
* Post-condition loops: `REPEAT ... UNTIL`
* Pre-condition loops: `WHILE ... ENDWHILE`

### Procedures and Functions

* `PROCEDURE ... ENDPROCEDURE` with parameter support
* `FUNCTION ... RETURNS ... ENDFUNCTION` with return values
* Parameter passing: `BYVAL`, `BYREF`

### File Handling

* Text files: `OPENFILE`, `READFILE`, `WRITEFILE`, `EOF`, `CLOSEFILE`
* Random files: `OPENFILE ... FOR RANDOM`, `SEEK`, `GETRECORD`, `PUTRECORD`

### Object-Oriented Programming

* Classes with `CLASS ... ENDCLASS`
* Public and private methods and properties (`PUBLIC`, `PRIVATE`)
* Constructors using `NEW`
* Inheritance with `INHERITS`, `SUPER` calls
* Object instantiation with `MyObject ← NEW MyClass(...)`

### Currently unsupported features from CAIE Pseudocode

* Values of enums are not type-casted to integers automatically. You must use `ord(<enum-value>)` and `<enum-name>(<integer>)` to type-cast between them. So you have to write `NextSeason <- Season(MyPointer^ + 1)` instead of `NextSeason <- MyPointer^ + 1`.
* Number ranges in case-statements do not yet support negative initial value, for example, `-10 TO 10: <case-body>`

## License

This project is licensed under the Free Personal Use License included in this repository. Redistribution and modification are not permitted.

## Contributing

This project does not currently accept contributions or pull requests.

