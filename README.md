# Scripts
# File Search Utility

This is a Python script that allows you to search for a file by its name across all available drives on a Windows system. It utilizes the `os` module to interact with the operating system and `string` module to generate a list of possible drive letters.

## Prerequisites

- Python 3.x
- Windows operating system

## Usage

1. Clone the repository or download the script `file_search.py` to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:

   ```
   python file_search.py
   ```

4. When prompted, enter the name of the file you want to search for **without** specifying the file extension.

5. The script will search all available drives (from A to Z) for the specified file. The search may take some time depending on the size and number of files on your drives.

6. Once the search is complete, the script will display the paths of any matching files found.

## Example

Here's an example to demonstrate how to use the script:

```
Enter file name: myfile
Please wait, Searching drives...
C:\Users\John\Documents\myfile
D:\Projects\myfile
```

In this example, the script searched for a file named "myfile" and found two matches, one located in `C:\Users\John\Documents` and another in `D:\Projects`.

## Limitations

- This script is designed to work specifically on Windows operating systems as it relies on drive letters.
- The script only searches for files in the root directories of the available drives. It does not recursively search subdirectories.
- The search process may take a long time if you have a large number of files or drives with a significant amount of data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.
