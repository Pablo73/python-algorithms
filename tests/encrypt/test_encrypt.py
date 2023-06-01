from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("MESSAGE", "2")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)

    assert encrypt_message("message", 4) == 'ega_ssem'

    assert encrypt_message("message", 3) == 'sem_egas'

    assert encrypt_message("message", 10) == 'egassem'
