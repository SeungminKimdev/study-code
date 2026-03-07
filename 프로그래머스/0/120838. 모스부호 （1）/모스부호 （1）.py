def solution(letter):
    answer = ''
    mos_all = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
           "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    letter_list = letter.split(' ')
    for alp in letter_list:
        answer += chr(mos_all.index(alp) + ord('a'))
    return answer