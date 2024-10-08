class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numer = numer1 * denom2 + numer2 * denom1;
        int denom = denom1 * denom2;
        int check = 2;
        while (check <= numer){
            if (numer % check == 0 && denom % check == 0){
                numer = numer / check;
                denom = denom / check;
                check = 2;
            }
            else{
                check++;
            }
        }
        int[] answer = {numer,denom};
        return answer;
    }
}