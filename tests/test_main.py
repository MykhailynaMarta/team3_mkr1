import pytest
from main import filter_file_by_keyword

def test_filter_file_by_keyword(tmp_path):
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("рядок без слова\nрядок з ключовим словом\nще один рядок")
    
    keyword = "ключовим"
    output_file = tmp_path / "filtered.txt"
    
    filter_file_by_keyword(str(test_file), keyword, str(output_file))
    
    assert output_file.read_text().strip() == "рядок з ключовим словом"

@pytest.mark.parametrize("content, keyword, expected", [
    ("рядок без слова\nключове слово тут\nще один рядок", "ключове", "ключове слово тут"),
    ("перше слово\nдруге слово\nтретє слово", "відсутнє", ""),
    ("ключове\nключове слово\nще ключове слово", "ключове", "ключове\nключове слово\nще ключове слово"),
])
def test_filter_variants(tmp_path, content, keyword, expected):
    test_file = tmp_path / "test_input.txt"
    test_file.write_text(content)
    output_file = tmp_path / "filtered.txt"
    
    filter_file_by_keyword(str(test_file), keyword, str(output_file))
    
    assert output_file.read_text().strip() == expected