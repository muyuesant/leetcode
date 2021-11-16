# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            plusIndex = local.find("+")
            if plusIndex > -1:
                local = local[0:plusIndex]
            # print("local", local, "domain", domain)
            email = local+"@"+domain
            # print(email)
            if email not in result:
                result.add(email)
        return len(result)