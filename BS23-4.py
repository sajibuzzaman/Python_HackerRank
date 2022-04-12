# Jerry Bhai
'''
Jerry is a playboy. He has a plan where he will meet at least one girl of a town in his country and provides her with deep love. He travels various towns and makes loves, as a result, his cost increases in most of the month. He travels on various routes and paths. But he does not like to ride on trains. The trains have more traffics and most of the days after buying the ticket, he couldn’t handle getting to the train. Even after pushing the crowd, he gets on the train, he sees there are already person sitting on his chair and they even don’t look at him. This is the scenario. But as he is very romantic, he must travel on the train And as he must reach early to various city from his city, he always takes path which is shortest.

There are xx towns which are denoted by 11 to xx. Jerry lives in town 11.The Town are Connected by pp pathways. The i-th path, Which connects town a_ia
i
​
  and b_ib
i
​
 . The length if i - thi−th path is c_ic
i
​
  kilometer . Jerry Can Move easily from town a_ia
i
​
  to b_ib
i
​
  and b_ib
i
​
  to a_ia
i
​
  by using the i-thi−th road

Lastly, There are also q train paths.The i - thi−th train path connects town t_it
i
​
  and town 11,where jerry live. which is w_iw
i
​
  kilometer long. The training path is also can be used to go from city 11 to town t_it
i
​
  and from town t_it
i
​
  to 11.

He always dreams at the time of riding. If he ever becomes president, he will lose some of the train routes. As he is busy planning to increase the number of girlfriends, so please tell Jerry the maximum number of train lines that can be shut down such that the length of the shortest path from every town to town 11 should remain the same as before.

Input
The first line contains three integers x, p, q (2 ≤ x ≤ 105; 1 ≤ p ≤ 3·105; 1 ≤ q ≤ 105).

Each of the next p lines contains three integers ai, bi, ci (1 ≤ ai, bi ≤ x; ai ≠ bi; 1 ≤ ci ≤ 109).

Each of the next q lines contains two integers ti and wi (2 ≤ ti ≤ x; 1 ≤ wi ≤ 109).

Every city will, without a doubt, have at least one route to the capital. It's worth noting that there may be many highways connecting the two cities. There may also be many paths from the town of Jerry to the same town.

Output
Output one single integer, the maximum number of train lines that can be shut down such that the length of the shortest path from every town to town 11 should remain the same as before.

Sample 1
Input
5 5 3
1 2 1
2 3 2
1 3 3
3 4 4
1 5 5
3 5
4 5
5 5

Output
2

Sample 2
Input
2 2 3
1 2 2
2 1 3
2 1
2 2
2 3

Output
2
'''