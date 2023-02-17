# bool consecutiveDucks(int n) {
#   for (int i = 0; i <= n ~/ 2; i++) {
#       int ans = 0;
#     for (int a = i + 1; a < n ~/ 2 ~/2; a++) {
#       ans += a;
#       if (ans == n) {
#         return true;
#       }
#     }
#   }
#   return false;
#   // your code here
# }

def consecutive_ducks(n):
    i = 0
    while i<=n//2:
        ans = 0
        a=i+1
        while a<n//2:
            ans +=a
            if  ans==n:
                return True
            a+=1
        i+=1
    return False

print(consecutive_ducks(10))