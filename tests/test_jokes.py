from mota import jokes


def test_direito_punchline_is_canonical():
    assert jokes.direito() == "Por quê, tô fazendo errado?"
    assert "Por quê, tô fazendo errado?" in jokes.tell("direito")


def test_by_id_returns_joke():
    joke = jokes.by_id("php")

    assert joke.id == "php"
    assert "PHP" in joke.setup


def test_new_example_jokes_are_available():
    assert "docker" in jokes.ids()
    assert "cache" in jokes.ids()
    assert "regex" in jokes.ids()
    assert "prod" in jokes.ids()


def test_docker_example_matches_readme():
    assert jokes.tell("docker") == (
        "O Mota colocou a piada ruim no Docker.\n"
        "Agora ela roda igual em qualquer máquina, infelizmente."
    )


def test_random_can_filter_by_tag():
    joke = jokes.random(tags=["python"])

    assert "python" in joke.tags


def test_audit_has_total():
    assert jokes.audit()["total"] == len(jokes.all())
    assert jokes.audit()["total"] >= 16


def test_search_finds_by_tag():
    results = jokes.search("python")

    assert results
    assert all("python" in joke.tags or "python" in str(joke).casefold() for joke in results)


def test_cringe_index_is_bounded():
    assert 0 <= jokes.cringe_index("direito") <= 100
