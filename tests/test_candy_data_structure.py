import pytest
from candy_problem.main import * 

def test_get_friends_favorite_candy_count():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    #Act
    new_popular_candy_dict = get_friends_favorite_candy_count(friend_favorites)

    #Assert
    assert new_popular_candy_dict["lollipop"] == 2


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict
    

def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", ["lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert

    assert new_candy_data["lollipop"] == ["Sally", "Bob"]