def read_datasets():
    """Read datasets and concatenate them"""
    datasets = []
    for k in range(5,10):
        datasets.append(pd.read_csv('Data/atp200{}.csv'.format(k)))
    for k in range(10,21):
        datasets.append(pd.read_csv('Data/atp20{}.csv'.format(k)))
    
    new_dataset = pd.DataFrame()
    for d in datasets:
        new_dataset = pd.concat((new_dataset, d), ignore_index=True)
    
    return new_dataset

def get_cumulated_set_won(dataset):
    
    dataset['CumSetWonA'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['CumSetWonB'] = np.zeros(len(dataset)).reshape(-1,1)
    
    players = np.unique(dataset[['Player A', 'Player B']])
    
    for player in players:
        warunek = (dataset['Player A'] == player) | (dataset['Player B'] == player)
        won_set = [0]
        indices = dataset[warunek].index
    
        for x in range(len(dataset[warunek])):
                if (dataset[warunek]['Player A'].iloc[x] == player):
                    won_set.append(dataset[warunek]['Asets'].iloc[x])
                else:
                    won_set.append(dataset[warunek]['Bsets'].iloc[x])
    
        for x in range(len(indices)):
                if (dataset.loc[indices[x], 'Player A'] == player):
                    dataset.loc[indices[x], 'CumSetWonA'] = np.cumsum(won_set)[x]
                else:
                    dataset.loc[indices[x], 'CumSetWonB'] = np.cumsum(won_set)[x]

def get_cumulated_set_lost(dataset):
    
    dataset['CumSetLostA'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['CumSetLostB'] = np.zeros(len(dataset)).reshape(-1,1)
    
    players = np.unique(dataset[['Player A', 'Player B']])
    
    for player in players:
        warunek = (dataset['Player A'] == player) | (dataset['Player B'] == player)
        lost_set = [0]
        indices = dataset[warunek].index
    
        for x in range(len(dataset[warunek])):
                if (dataset[warunek]['Player A'].iloc[x] == player):
                    lost_set.append(dataset[warunek]['Bsets'].iloc[x])
                else:
                    lost_set.append(dataset[warunek]['Asets'].iloc[x])
    
        for x in range(len(indices)):
                if (dataset.loc[indices[x], 'Player A'] == player):
                    dataset.loc[indices[x], 'CumSetLostA'] = np.cumsum(lost_set)[x]
                else:
                    dataset.loc[indices[x], 'CumSetLostB'] = np.cumsum(lost_set)[x]
                    
def sum_games_won_for_each_match(dataset):
    dataset['Agames'] = dataset[['A1', 'A2', 'A3', 'A4', 'A5']].sum(axis=1)
    dataset['Bgames'] = dataset[['B1', 'B2', 'B3', 'B4', 'B5']].sum(axis=1)

def get_cumulated_games_won(dataset):
    
    dataset['CumGamesWonA'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['CumGamesWonB'] = np.zeros(len(dataset)).reshape(-1,1)
    
    players = np.unique(dataset[['Player A', 'Player B']])
    
    for player in players:
        warunek = (dataset['Player A'] == player) | (dataset['Player B'] == player)
        won_games = [0]
        indices = dataset[warunek].index
    
        for x in range(len(dataset[warunek])):
                if (dataset[warunek]['Player A'].iloc[x] == player):
                    won_games.append(dataset[warunek]['Agames'].iloc[x])
                else:
                    won_games.append(dataset[warunek]['Bgames'].iloc[x])
    
        for x in range(len(indices)):
                if (dataset.loc[indices[x], 'Player A'] == player):
                    dataset.loc[indices[x], 'CumGamesWonA'] = np.cumsum(won_games)[x]
                else:
                    dataset.loc[indices[x], 'CumGamesWonB'] = np.cumsum(won_games)[x]

def get_cumulated_games_lost(dataset):
    
    dataset['CumGamesLostA'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['CumGamesLostB'] = np.zeros(len(dataset)).reshape(-1,1)
    
    players = np.unique(dataset[['Player A', 'Player B']])
    
    for player in players:
        warunek = (dataset['Player A'] == player) | (dataset['Player B'] == player)
        lost_games = [0]
        indices = dataset[warunek].index
    
        for x in range(len(dataset[warunek])):
                if (dataset[warunek]['Player A'].iloc[x] == player):
                    lost_games.append(dataset[warunek]['Bgames'].iloc[x])
                else:
                    lost_games.append(dataset[warunek]['Agames'].iloc[x])
    
        for x in range(len(indices)):
                if (dataset.loc[indices[x], 'Player A'] == player):
                    dataset.loc[indices[x], 'CumGamesLostA'] = np.cumsum(lost_games)[x]
                else:
                    dataset.loc[indices[x], 'CumGamesLostB'] = np.cumsum(lost_games)[x]
                    
def perc_set_won(dataset):
    
    for x in range(len(dataset)):
        if ((dataset.loc[x, 'CumSetWonA']==0) & (dataset.loc[x, 'CumSetLostA']==0)):
            dataset.loc[x, '%SetWinA'] = 0
        else:
            dataset.loc[x, '%SetWinA'] = dataset.loc[x, 'CumSetWonA']/(dataset.loc[x, 'CumSetWonA']+dataset.loc[x, 'CumSetLostA'])
                               
        if ((dataset.loc[x, 'CumSetWonB']==0) & (dataset.loc[x, 'CumSetLostB']==0)):
            dataset.loc[x, '%SetWinB'] = 0
        else:
            dataset.loc[x, '%SetWinB'] = dataset.loc[x, 'CumSetWonB']/(dataset.loc[x, 'CumSetWonB']+dataset.loc[x, 'CumSetLostB'])
          
def perc_games_won(dataset):
    
    for x in range(len(dataset)):
        if ((dataset.loc[x, 'CumGamesWonA']==0) & (dataset.loc[x, 'CumGamesLostA']==0)):
            dataset.loc[x, '%GamesWinA'] = 0
        else:
            dataset.loc[x, '%GamesWinA'] = dataset.loc[x, 'CumGamesWonA']/(dataset.loc[x, 'CumGamesWonA']+dataset.loc[x, 'CumGamesLostA'])
                               
        if ((dataset.loc[x, 'CumGamesWonB']==0) & (dataset.loc[x, 'CumGamesLostB']==0)):
            dataset.loc[x, '%GamesWinB'] = 0
        else:
            dataset.loc[x, '%GamesWinB'] = dataset.loc[x, 'CumGamesWonB']/(dataset.loc[x, 'CumGamesWonB']+dataset.loc[x, 'CumGamesLostB'])
            
def cumulated_set_won_depend_on_surface(dataset):
    
    dataset['CumSetWonASurface'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['CumSetWonBSurface'] = np.zeros(len(dataset)).reshape(-1,1)
    
    surfaces = np.unique(dataset['Surface'])
    
    players = np.unique(dataset[['Player A', 'Player B']])
    
    for surface in surfaces:
    
        for player in players:
            warunek = (((dataset['Player A'] == player) | (dataset['Player B'] == player)) & (dataset['Surface'] == surface))
            won_set = [0]
            indices = dataset[warunek].index


            for x in range(len(dataset[warunek])):
                    if (dataset[warunek]['Player A'].iloc[x] == player):
                        won_set.append(dataset[warunek]['Asets'].iloc[x])
                    else:
                        won_set.append(dataset[warunek]['Bsets'].iloc[x])

            for x in range(len(indices)):
                    if (dataset.loc[indices[x], 'Player A'] == player):
                        dataset.loc[indices[x], 'CumSetWonASurface'] = np.cumsum(won_set)[x]
                    else:
                        dataset.loc[indices[x], 'CumSetWonBSurface'] = np.cumsum(won_set)[x]
                        
def cumulated_set_lost_depend_on_surface(dataset):
    
    dataset['CumSetLostASurface'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['CumSetLostBSurface'] = np.zeros(len(dataset)).reshape(-1,1)
    
    surfaces = np.unique(dataset['Surface'])
    
    players = np.unique(dataset[['Player A', 'Player B']])
    
    for surface in surfaces:
    
        for player in players:
            warunek = (((dataset['Player A'] == player) | (dataset['Player B'] == player)) & (dataset['Surface'] == surface))
            lost_set = [0]
            indices = dataset[warunek].index

            for x in range(len(dataset[warunek])):
                    if (dataset[warunek]['Player A'].iloc[x] == player):
                        lost_set.append(dataset[warunek]['Bsets'].iloc[x])
                    else:
                        lost_set.append(dataset[warunek]['Asets'].iloc[x])

            for x in range(len(indices)):
                    if (dataset.loc[indices[x], 'Player A'] == player):
                        dataset.loc[indices[x], 'CumSetLostASurface'] = np.cumsum(lost_set)[x]
                    else:
                        dataset.loc[indices[x], 'CumSetLostBSurface'] = np.cumsum(lost_set)[x]
                        
def cumulate_wins_and_loses(dataset):
    
    dataset['WinsA'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['LosesA'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['WinsB'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['LosesB'] = np.zeros(len(dataset)).reshape(-1,1)
    
    players = np.unique(dataset[['Player A', 'Player B']])

    for player in players:

        warunek = (dataset['Player A'] == player) | (dataset['Player B'] == player)
        match_won = [0]
        match_lost = [0]
        indices = dataset[warunek].index

        for x in range(len(indices)):
            if (((dataset[warunek]['Player A'].iloc[x] == player) & (dataset[warunek]['Result'].iloc[x] == 1)) | ((dataset[warunek]['Player B'].iloc[x] == player) & (dataset[warunek]['Result'].iloc[x] == 0))):
                match_won.append(1)
                match_lost.append(0)
            else:
                match_won.append(0)
                match_lost.append(1)

        for x in range(len(indices)):
                if (dataset.loc[indices[x], 'Player A'] == player):
                    dataset.loc[indices[x], 'WinsA'] = np.cumsum(match_won)[x]
                    dataset.loc[indices[x], 'LosesA'] = np.cumsum(match_lost)[x]
                else:
                    dataset.loc[indices[x], 'WinsB'] = np.cumsum(match_won)[x]
                    dataset.loc[indices[x], 'LosesB'] = np.cumsum(match_lost)[x]
                    
def b365_pred(dataset):

    dataset['b365_pred'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['b365_pred'][dataset['B365A']<dataset['B365B']] = 1

def ps_pred(dataset):

    dataset['ps_pred'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['ps_pred'][dataset['PSA']<dataset['PSB']] = 1

def rank_pred(dataset):

    dataset['rank_pred'] = np.zeros(len(dataset)).reshape(-1,1)
    dataset['rank_pred'][dataset['ARank']<dataset['BRank']] = 1
    
def perc_set_won_surface(dataset):
    
    for x in range(len(dataset)):
        if ((dataset.loc[x, 'CumSetWonASurface']==0) & (dataset.loc[x, 'CumSetLostASurface']==0)):
            dataset.loc[x, '%SetWinASurface'] = 0
        else:
            dataset.loc[x, '%SetWinASurface'] = dataset.loc[x, 'CumSetWonASurface']/(dataset.loc[x, 'CumSetWonASurface']+dataset.loc[x, 'CumSetLostASurface'])
                               
        if ((dataset.loc[x, 'CumSetWonBSurface']==0) & (dataset.loc[x, 'CumSetLostBSurface']==0)):
            dataset.loc[x, '%SetWinBSurface'] = 0
        else:
            dataset.loc[x, '%SetWinBSurface'] = dataset.loc[x, 'CumSetWonBSurface']/(dataset.loc[x, 'CumSetWonBSurface']+dataset.loc[x, 'CumSetLostBSurface'])
            
def perc_match_won(dataset):
    
    for x in range(len(dataset)):
        if ((dataset.loc[x, 'WinsA']==0) & (dataset.loc[x, 'LosesA']==0)):
            dataset.loc[x, '%MatchWinA'] = 0
        else:
            dataset.loc[x, '%MatchWinA'] = dataset.loc[x, 'WinsA']/(dataset.loc[x, 'WinsA']+dataset.loc[x, 'LosesA'])
                               
        if ((dataset.loc[x, 'WinsB']==0) & (dataset.loc[x, 'LosesB']==0)):
            dataset.loc[x, '%MatchWinB'] = 0
        else:
            dataset.loc[x, '%MatchWinB'] = dataset.loc[x, 'WinsB']/(dataset.loc[x, 'WinsB']+dataset.loc[x, 'LosesB'])