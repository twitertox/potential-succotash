TeamName = ["a","b","c"];
Teampoints = [[2,3,0,1],[2,3,2,2],[3,0,0,1]];
high = [];
low = [];
MatchNo = 4;
Leaguesize = 3;
def totalpoints():
    for counter in range(Leaguesize):
        total = 0
        point = "";
        aw = 0
        hw = 0
        d = 0
        lm = 0
        for number in range(MatchNo):
            total = Teampoints[counter][number] + total
            if Teampoints[counter][number] == 3:
                point = "away win"
                aw = aw + 1
            elif Teampoints[counter][number] == 2:
                point = "home win"
                hw = hw + 1
            elif Teampoints[counter][number] == 1:
                point = "draw"
                d = d + 1
            else:
                point = "lost match"
                lm = lm + 1
            print(TeamName[counter],total,"number of away win are",aw,"number of home win is", hw,"number of draw matches are",d,"number of lost matches are",lm)


def highest_point(TeamName,Teampoints,high,low):
    for counter in range(Leaguesize):
        total = 0
        for number in range(MatchNo):
            total = Teampoints[counter][number] + total
        high.append(total)
        low.append(total)
    for counter in range(len(high)):
        for number in range(len(high)):
            if high[counter] < high[counter + 1]:
                high[counter],high[counter + 1] = high[counter + 1],high[counter]
                TeamName[counter],TeamName[counter + 1] = TeamName[counter + 1],TeamName[counter]
        return TeamName,high
    print(TeamName[1],"Team with highest point")    
    for counter in range(len(low)):
        for number in range(len(low)):
            if low[counter] > low[counter + 1]:
                low[counter],low[counter + 1] = low[counter + 1],low[counter]
                TeamName[counter],TeamName[counter + 1] = TeamName[counter + 1],TeamName[counter]
        return TeamName,low
    print(TeamName[1],"Scored lowest")

highest_point(TeamName,Teampoints,high,low)

        

