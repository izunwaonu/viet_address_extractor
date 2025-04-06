# Vietnamese Address Extractor

This project extracts **province**, **district**, and **ward** information from Vietnamese address text using a **Trie-based** matching algorithm. It is developed according to the course assignment specifications.

GitHub: [https://github.com/izunwaonu/viet_address_extractor](https://github.com/izunwaonu/viet_address_extractor)

---

## 📁 Project Structure

```
viet_address_extractor/
├── data/
│   ├── list_province.txt       # List of provinces
│   ├── list_district.txt       # List of districts
│   ├── list_ward.txt           # List of wards
│   └── test.json               # Input test dataset (required for evaluation)
├── solution/
│   ├── extractor.py            # Main logic to extract address components
├── trie/
│   ├── trie.py                 # Trie data structure
│   └── trie_node.py            # Trie node class
├── test_runner.py              # Evaluation script
├── requirements.txt            # Python packages to install
└── README.md                   # This file
```

---

## 🚀 How to Run

Follow the steps below to run the project and evaluate your implementation.

### 1. Clone the Repository

```bash
git clone https://github.com/izunwaonu/viet_address_extractor.git
cd viet_address_extractor
```

### 2. Install Required Packages

Make sure you have Python installed (Python 3.7+ recommended). Then install dependencies:

```bash
pip install -r requirements.txt
```

This installs packages like:

- `pandas`
- `xlsxwriter`

### 3. Prepare Test Data

Make sure the following files exist inside the `data/` folder:

- `test.json` — contains address samples and expected results.
- `list_province.txt` — list of all provinces.
- `list_district.txt` — list of all districts.
- `list_ward.txt` — list of all wards.

Each `.txt` file must contain **one entry per line**.

Sample format for `test.json`:

```json
[
  {
    "text": "Số 1 Lê Duẩn, Quận 1, TP HCM",
    "result": {
      "province": "Hồ Chí Minh",
      "district": "Quận 1",
      "ward": "Phường Bến Nghé"
    }
  },
  ...
]
```

---

### 4. Run the Evaluation

To test and evaluate the solution, run the command:

```bash
python test_runner.py
```

This will execute the extractor and export results into an Excel file.

---

## 📊 Output

After running the script, you will see a file like:

```bash
TEAM_THREE.xlsx
```

It contains one excel file with two sheets:

1. **summary** — includes:
   - Total correct predictions.
   - Overall score out of 10.
   - Maximum and average execution time per test case.

2. **details** — includes:
   - Original input address.
   - Ground-truth vs extracted values for province, district, and ward.
   - Normalized versions of all fields.
   - Whether each prediction was correct (`1` for correct, `0` for incorrect).
   - Time taken for that row.

Example columns in the `details` sheet:

```
ID | text | province | province_student | province_correct | ... | time_sec
```

---

## ✅ Notes

- Matching is case-insensitive and supports normalization (e.g., "TP HCM" is treated as "Hồ Chí Minh").
- Trie is used for efficient and fast longest-prefix matching.
- You can extend the normalization dictionaries in `extractor.py` for better accuracy.
- The project is structured for clarity, performance, and strict adherence to the lecturer’s specifications.

---

## 🧠 Authors
- Team Name: `TEAM_THREE`
- GitHub: [MD KAMRUZZAMAN RUSSEL](https://github.com/KAMRUZZAMAN-RUSSEL)
- GitHub: [Felix Luca Krebs](https://github.com/XDcobra)
- GitHub: [Justus Izuchukwu Onuh](https://github.com/izunwaonu)

---

## 🛠 Requirements File

Ensure your `requirements.txt` looks like this:

```
pandas
xlsxwriter
```

Install with:

```bash
pip install -r requirements.txt
```

---


