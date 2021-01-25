class Solution {
   public int firstUniqChar(String s) {
        var charArr = s.toCharArray();
        char[] charMap = createCharMap(charArr);
        return getFirstIndexOfUniqueChar(charArr, charMap);
    }

    private char[] createCharMap(char[] charArr) {
        var charMap = new char['z'-'a'+1];
        for(var ch : charArr){
            charMap[ch - 'a']++;
        }
        return charMap;
    }

    private int getFirstIndexOfUniqueChar(char[] charArr, char[] charMap) {
        int firstUnique = -1;
        for(int i = 0; i< charArr.length; i++){
            if( charMap[ charArr[i] - 'a'] == 1) {
                firstUnique = i;
                break;
            }
        }
        return firstUnique;
    }

}
