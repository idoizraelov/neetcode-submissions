class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i,email in enumerate(emails):
            local_name , domain = email.split('@')
            local_name=local_name.split('+')[0]
            local_name=local_name.replace('.','')
            clean_mail=local_name+'@'+domain
            emails[i]=clean_mail
            
        
        return len(set(emails))

            