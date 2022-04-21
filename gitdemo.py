# Some football variables
favorite_team = 'Manchester City'
favorite_player = 'Joao Cancelo'

transfer_target = 'Erling Haaland'
greatest_ginger_athlete = 'Kevin De Bruyne'

def __oints(points):
        l0 = set()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if points[i][0] == points[j][0]:
                    m = 'vertical'
                    b = points[i][0]
                else:
                    m = (points[i][1]-points[j][1])/(points[i][0]-points[j][0])
                    b = points[i][1]-m*points[i][0]
                l0.add((m, b))
        print(l0)
        ans = 1
        for line in l0:
            counter = 0
            for point in points:
                if line[0] == 'vertical':
                    if point[0] == line[1]:
                        counter+=1
                elif round(point[1], 10) == round(line[0]*point[0]+line[1], 10):
                    counter += 1
            if counter > ans:
                ans = counter
        return ans


lineup = {'CB': 'ImEric TheDoor', 'K': 'Ederson Moraes', 'LB': favorite_player, 'CAM': greatest_ginger_athlete}


__oints([[1,1],[2,2],[3,3]])

for position in lineup:
    print(f'{position}: {lineup[position]}')