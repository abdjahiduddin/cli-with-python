
# Logs CLI - Technical Test

Logs CLI merupakan tools untuk mengambil logs file kemudian melakukan konversi menjadi JSON atau Text. Logs CLI dibangun menggunakan Python 3.


## Library

**Typer:** Library ini digunakan untuk membuat CLI Tools.

**os:** Library os digunakan untuk membuat directory, memeriksa apakah sebuah file atau directory ada, dan membuat Path dengan menggabungkan lokasi file dan nama file.  

**pathlib:** Library ini digunakan untuk mendapatkan Path dari Home Directory dan mengekstrak nama file dari Path yang dimasukkan User.

## Run Locally

Clone project

```bash
  git clone https://github.com/abdjahiduddin/cli-with-python.git
```

Masuk ke directory project 

```bash
  cd cli-with-python
```

Membuat virtual environment (Optional)

```bash
  python3 -m venv ./venv
  source venv/bin/activate
```

Install libraries

```bash
  python3 -m pip install -r requirements.txt
```

Jalankan perintah berikut untuk mengonfirmasi versi Logs CLI

```bash
  python3 -m logs --version
```


## Logs CLI Documentation

## `python3 -m logs`

Convert Logs file to JSON or TEXT.

**Usage**:

```console
$ logs [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* ` -v, --version`: Show application's version and exit.
* `--help`: Show this message and exit.

**Commands**:

* `get`: Get Logs File.

## `python3 -m logs get`

Get Logs File.

**Usage**:

```console
$ logs get [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]


**Options**:

* `-t`: Output type [json|text]  [default: text]
* `-o`: Destination path  [default: /home/jay/logs-converter-output]
* `--help`: Show this message and exit.


## Screenshots
* Get dpkg.log and convert to text
![text-default](https://github.com/abdjahiduddin/cli-with-python/blob/main/img/text-default.png?raw=true)

* Get dpkg.log and convert to json
![json-default](https://github.com/abdjahiduddin/cli-with-python/blob/main/img/json-default.png?raw=true)

* Get dpkg.log, convert to json and save to custom path
![json-custom](https://github.com/abdjahiduddin/cli-with-python/blob/main/img/json-custom.png?raw=true)

* Get dpkg.log, convert to text and save to custom path
![text-custom](https://github.com/abdjahiduddin/cli-with-python/blob/main/img/text-custom.png?raw=true)


* Show help for `logs` command
![logs-help](https://github.com/abdjahiduddin/cli-with-python/blob/main/img/logs-help.png?raw=true)

* Show help for `logs get` command
![logs-get-help](https://github.com/abdjahiduddin/cli-with-python/blob/main/img/logs-get-help.png?raw=true)

* Show Logs CLI version

![logs-get-help](https://github.com/abdjahiduddin/cli-with-python/blob/main/img/version.png?raw=true)
