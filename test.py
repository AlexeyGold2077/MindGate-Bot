import mindgate_pywrapper

print(mindgate_pywrapper.getBalance(123))
print(mindgate_pywrapper.addBalance(123, 1000))
print(mindgate_pywrapper.getBalance(123))
print(mindgate_pywrapper.sendMessageAsSystem(123, "be very breif"))
print(mindgate_pywrapper.sendMessageAsUser(123, "hi"))
print(mindgate_pywrapper.getBalance(123))
print(mindgate_pywrapper.sendMessageAsUser(123, "напиши очень короткий стих"))
print(mindgate_pywrapper.getBalance(123))
print(mindgate_pywrapper.clearMessages(123))
print(mindgate_pywrapper.getModel(123))
print(mindgate_pywrapper.setModel(123, "gpt-4o"))
print(mindgate_pywrapper.getModel(123))
