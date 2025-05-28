class Solution {
    public boolean isNumber(String s) {
        s = s.trim(); // Remove leading/trailing whitespaces

        if (s.isEmpty()) return false;

        int eIndex = Math.max(s.indexOf('e'), s.indexOf('E'));

        if (eIndex != -1) {
            String base = s.substring(0, eIndex);
            String exp = s.substring(eIndex + 1);
            return (isDecimal(base) || isInteger(base)) && isInteger(exp);
        }

        return isDecimal(s) || isInteger(s);
    }

    private boolean isInteger(String s) {
        if (s.isEmpty()) return false;

        if (s.charAt(0) == '+' || s.charAt(0) == '-') {
            s = s.substring(1);
        }

        return isAllDigits(s);
    }

    private boolean isDecimal(String s) {
        if (s.isEmpty()) return false;

        if (s.charAt(0) == '+' || s.charAt(0) == '-') {
            s = s.substring(1);
        }

        int dotIndex = s.indexOf('.');
        if (dotIndex == -1) return false;

        String left = s.substring(0, dotIndex);
        String right = s.substring(dotIndex + 1);

        // Both sides shouldn't be empty
        if (left.isEmpty() && right.isEmpty()) return false;

        return (left.isEmpty() || isAllDigits(left)) &&
               (right.isEmpty() || isAllDigits(right));
    }

    private boolean isAllDigits(String s) {
        if (s.isEmpty()) return false;

        for (char ch : s.toCharArray()) {
            if (!Character.isDigit(ch)) return false;
        }

        return true;
    }
}