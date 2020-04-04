# We can append or pop items from and to stack, stacks uses
# LIFO metod for appending and removing item from lists
# LIFO is Last(element) In First(element) Out
# See this browsing seession examples bellow:

browsing_session = ["Page 1", "Page 2", "Page 3"]
browsing_session.append("Page 4")
print(browsing_session)
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]  # redirect to the last page

print(browsing_session)
