# generate_questions_for_quiz

Python scripts that generate quiz question JSON files from raw vocabulary CSV data. Used to build the question banks for the [QuizPulse](https://github.com/rostam/quizpulse) language learning projects.

## Scripts

| Script | What it generates |
|--------|------------------|
| `generate_questions_for_quiz.py` | Translation questions (word → meaning, 4-choice MCQ) |
| `generate_antonyms.py` | Antonym questions from paired word lists |
| `generate_numbers_questions.py` | Number quizzes (e.g. Korean native number system) |
| `process_amazon_files.py` | Pre-processes Amazon vocabulary datasets |

## Input format

CSV files with vocabulary data, one word/phrase pair per row. Language folders (`Arabic/`, `English/`, `German/`, `Korean/`, `Persian/`, `Spanish/`, `Turkish/`) each contain their source CSVs.

Example column layout:
```
index, native_word, translation
```

## Output format

JSON array of question objects consumed by QuizPulse:
```json
[
  {
    "question": "안녕하세요",
    "choices": ["Hello", "Goodbye", "Thank you", "Sorry"],
    "answer": 0,
    "type": "ko_en",
    "extra": ""
  }
]
```

## Usage

```bash
python generate_questions_for_quiz.py
```

Edit the script to point `input` at your CSV and `output` at the target JSON path, and set `type1`/`type2` to your language pair identifier.

## Requirements

```bash
pip install -r requirements.txt  # standard library only — no extra deps needed
```
