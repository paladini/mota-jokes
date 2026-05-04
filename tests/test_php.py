from mota import php


def test_is_php_accepts_php_neighbors():
    assert php.is_php("PHP")
    assert php.is_php("Laravel")
    assert not php.is_php("Python")


def test_translate_keeps_original_as_comment():
    translated = php.translate("print('ola')")

    assert translated.startswith("<?php")
    assert "print('ola')" in translated


def test_roast_mentions_php():
    assert "PHP" in php.roast()
    assert "vírgula" in php.roast()


def test_semicolon_adds_missing_semicolon():
    assert php.semicolon("$mota = 'meme'") == "$mota = 'meme';"
    assert php.semicolon("$mota = 'meme';") == "$mota = 'meme';"


def test_composer_install_mentions_package():
    output = php.composer_install("mota/humor")

    assert "composer require mota/humor" in output
    assert "configuração" in output


def test_composer_install_readme_example():
    assert php.composer_install("mota/bom-senso") == (
        "composer require mota/bom-senso\n"
        "Pacote instalado. O humor ainda requer configuração manual."
    )


def test_ini_get_has_fake_defaults():
    assert "On" in php.ini_get("display_errors")
