import pandas as pd


def load_nba_data() -> pd.DataFrame:
    """Load nba data for the 22/23 season as a Pandas Dataframe

    Returns:
        pd.DataFrame: stats for the 22/23 season
    """
    return pd.read_csv('22:23_player_stats.csv')

def player_profile() -> list:
    """Creates a list of dictionaries containing player bio data

    Returns:
        list: list of player data
    """
    df = load_nba_data()
    player_df = df.filter(regex = "rank|player|position|age|team")
    players_bio = [create_player_bio_dict(player) for i,player in player_df.iterrows()]
    return players_bio

def create_player_bio_dict(player:pd.DataFrame) -> dict:
    """Formats data that would be present in a player's bio

    Args:
        player (pd.DataFrame): a single player's details

    Returns:
        dict: formatted bio data
    """
    return {
        'player_id':player['rank'],
        'first_name':player['player'].split(' ')[0],
        'surname':player['player'].split(' ')[1],
        'position':player['position'],
        'age':player['age'],
        'team':player['team']
    }

def player_profiles_by_id(ids: list) -> list:
    """Gets the bios of players who have been requested by id

    Args:
        ids (list): list of player ids

    Returns:
        list: list of the selected players' bios 
    """
    all_bios = player_profile()
    list_of_ids = [int(id) for id in ids]
    requested_bios = [bio for bio in all_bios if bio['player_id'] in list_of_ids]
    return requested_bios