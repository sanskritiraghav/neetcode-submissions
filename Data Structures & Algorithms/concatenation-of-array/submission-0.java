class Solution {
    public int[] getConcatenation(int[] nums) {
        int [] ans = new int[nums.length + nums.length];
        ans = IntStream.concat(Arrays.stream(nums),Arrays.stream(nums)).toArray();
        return ans;
    }
}