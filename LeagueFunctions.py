import requests
import os

class LoL():
    def findSummonerID(self, summoner):
        url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner + '?api_key=' + str(os.environ.get('KEY'))
        r = requests.get(url)
        json_obj = r.json()
        return json_obj ['id']

    def getRank(self, ID):
        url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + str(ID) + '?api_key=' + str(os.environ.get('KEY'))
        r = requests.get(url)
        json_obj = r.json()
        rank_format = 'Unranked'
        j = 0
        for indice in json_obj:
            if json_obj[j]['queueType'] == 'RANKED_SOLO_5x5':
                rank = [json_obj[j]['tier'], json_obj[j]['rank'], json_obj[j]['leaguePoints']]
                print(json_obj[j]['queueType'])
                rank_format = rank[0] + ' ' + rank[1] + ' (' + str(rank[2]) + ' LP)'
                return rank_format
            else:
                j += 1
                rank = []
        return rank_format

    def getCurrentMatchSummoners(self, ID):
        url = 'https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/' + ID + '?api_key=' + str(os.environ.get('KEY'))
        r = requests.get(url)
        json_obj = r.json()
        n=0
        currentSummonerNames = []
        currentSummonerIDs = []
        teamIDs = []
        championIDs = []
        teamRanks = []
        while n < 10:
             currentSummonerIDs.append(self.findSummonerID(json_obj['participants'][n]['summonerName']))
             currentSummonerNames.append(json_obj['participants'][n]['summonerName'])
             teamIDs.append(json_obj['participants'][n]['teamId'])
             championIDs.append(json_obj['participants'][n]['championId'])
             teamRanks.append(self.getRank(self.findSummonerID(json_obj['participants'][n]['summonerName'])))
             n+=1
        return [currentSummonerNames, currentSummonerIDs, teamIDs, championIDs, teamRanks]

    def findChampionName(self, championID):
        url = 'http://ddragon.leagueoflegends.com/cdn/9.13.1/data/en_US/champion.json'
        r = requests.get(url)
        json_obj = r.json()
        data = json_obj['data']
        for name, attributes in data.items():
            if attributes['key'] == str(championID):
                return name

    def teammaker(self, summonerList, teamIds, championIDs, teamRanks):
        n=0
        Team1 = []
        Team1Champs = []
        Team1Ranks = []
        while n < 10:
            if teamIds[n] == 100:
                Team1.append(summonerList[n])
                Team1Champs.append(self.findChampionName(championIDs[n]))
                Team1Ranks.append(teamRanks[n])
            n+=1

        Team2 = []
        Team2Champs = []
        Team2Ranks = []
        n=0
        while n < 10:
            if teamIds[n] == 200:
                Team2.append(summonerList[n])
                Team2Champs.append(self.findChampionName(championIDs[n]))
                Team2Ranks.append(teamRanks[n])
            n += 1
        return [Team1, Team2, Team1Champs, Team2Champs, Team1Ranks, Team2Ranks]

