import random
''' 
发牌：由庄家开始发牌，轮流发给闲张第一张，庄家停牌后，系统再给闲家发牌。
要牌：玩家可以根据自己底牌的点数选择是否要牌，最多可以要4张。
点牌：A、2、3、4、5、6、7、9、10，其中A为1点其他牌为本身的点数。
人牌：大小王、J、Q、K被称为“人牌”，都算做半点。

人五小：5张人牌。
五小：5张牌不都是人牌，且总点数小于十点半。
十点半：5张牌以下，牌的总点数等于十点半。
牌型大小：人五小>五小>十点半>十点半以下
十点半以下以点数比较大小，庄家分别和每个闲家比较大小，失败者则输掉底注。（10点>9点半>9点>....>1点>0点半）
提示：当点数相同时，牌张数多者胜。同点同张的话，庄家胜。 
'''


def get_shuffled_deck():
    """初始化包括52张扑克牌的列表，并混排后返回，表示一副洗好的扑克牌"""
    # 花色suits和序号
    suits = {'♣', '♠', '♦', '♥'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    deck = [suit+' '+rank for rank in ranks for suit in suits]
    # 添加大小王
    deck.append('@ L')
    deck.append('@ S')
    random.shuffle(deck)
    return deck


def deal_card(deck, participant):
    """发一张牌给参与者participant"""
    participant.append(deck.pop())


def compute_total(hand):
    """计算并返回一手牌的点数和"""
    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 0.5, 'Q': 0.5, 'K': 0.5, 'L': 0.5, 'S': 0.5}
    result = 0  # 初始化点数和为0
    numAces = 0  # 人牌的个数

    # 计算点数和的人牌个数
    for card in hand:
        result += values[card[2:]]
        if card[2] in ['J', 'Q', 'K', 'L', 'S']:
            numAces += 1
    if result == 10.5 and len(hand) < 5:
        return "十点半"
    elif len(hand) == 5 and result < 10.5 and numAces:
        return "五小"
    elif numAces == 5:
        return "人五小"
    else:
        return result


def tenPointAndAHalf():
    """十点半牌游戏，计算机人工智能AI为庄家，用户为玩家"""
    # 初始化一副洗好的扑克牌，初始化庄家和玩家手中的牌为空
    deck = get_shuffled_deck()
    house = []  # 庄家的牌
    player = []  # 玩家的牌

    # 依次给玩家和庄家各发一张牌
    deal_card(deck, player)
    deal_card(deck, house)

    # 打印一手牌
    print('庄家的牌：'+','.join(house))
    print('玩家的牌：'+','.join(player))

    # 比较牌点
    houseTotal, playerTotal = compute_total(house), compute_total(player)
    if houseTotal > playerTotal:
        print('庄家赢牌!')
    elif houseTotal < playerTotal:
        print('玩家赢牌!')

    # 询问玩家是否继续拿牌，如果是，继续给玩家发牌
    while answer := input('是否继续拿牌（y/n，缺省为y）：') in ('', 'y', 'Y'):
        deal_card(deck, player)
        print('玩家的牌：'+','.join(player))

        # 计算牌点
        if compute_total(player) == "人五小":
            if compute_total(house) == "人五小":
                print("平局")
            else:
                print("玩家赢了")
            return
        elif compute_total(player) == "人五":
            if compute_total(house) == "人五小":
                print("庄家赢了")
            elif compute_total(house) == "人五":
                print("平局")
            else:
                print("玩家赢了")
            return
        elif compute_total(player) == "十点半":
            if compute_total(house) == "人五小" or compute_total(house) == "人五":
                print("庄家赢了")
            elif compute_total(house) == "十点半":
                print("平局")
            else:
                print("玩家赢了")
            return
        else:
            houseTotal, playerTotal = compute_total(
                house), compute_total(player)
            if playerTotal > houseTotal:
                print("玩家赢了")
            elif playerTotal < houseTotal:
                print("庄家赢了")
            else:
                print("平局")
        # 庄家(计算机人工智能)按“庄家规则”确定是否拿牌
        if len(house) < 5:
            deal_card(deck, house)
            print('庄家的牌：'+','.join(house))
        if len(player) == 5 and len(house) == 5:
            break


if __name__ == '__main__':
    tenPointAndAHalf()
