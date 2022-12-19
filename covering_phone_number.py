def solution(phone_number):
    num1 = len(phone_number)-4
    num2 = phone_number[-4:]
    answer = "*"*num1 + num2
    return answer








solution("01033334444")
solution("027778888")