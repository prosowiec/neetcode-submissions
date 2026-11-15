class Solution {
    public boolean isValid(String s) {
        Map<String, String> checkP = Map.of(
            "}", "{",
            "]", "[",
            ")", "("
        );        
        Deque<String> stack = new ArrayDeque<>();

        for (String e : s.split("")){
            if (checkP.keySet().contains(e) && stack.isEmpty()) return false;
            else if (checkP.keySet().contains(e)){
                String poped = stack.pop();
                if (!checkP.get(e).equals(poped)) return false;
            } else {
                stack.push(e);
            }
        }

        return stack.isEmpty();
    }
}
