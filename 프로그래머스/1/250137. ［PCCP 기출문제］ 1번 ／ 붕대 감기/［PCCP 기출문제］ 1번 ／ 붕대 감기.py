def solution(bandage, health, attacks):
    hp = health
    hTime, tHeal, addHeal = bandage
    beforeAT = 0
    for aT,aD in attacks:
        tempT = aT - beforeAT - 1
        hp += tempT * tHeal + addHeal * (tempT // hTime) 
        if hp > health:
            hp = health
        hp -= aD
        if hp <= 0:
            return -1
        beforeAT = aT
    return hp