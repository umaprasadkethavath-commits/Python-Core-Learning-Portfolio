employe_registry={
    "EMP501":{"name":"uma","clearance":"level_3","status":"active"},
    "EMP502":{"name":"rebal","clearance":"level_1","status":"suspended"},
    "EMP503":{"name":"salaar","clearance":"level_2","status":"active"}
}
cleaned_token_code="no token is asked employee may be suspended or access is denied "
employee_status="not registered "
user_id=input("Enter user id :")
cleaned_id=user_id.strip().upper()
if cleaned_id in employe_registry:
    employee_status=employe_registry[cleaned_id]["status"]
    if employee_status =="active":
        if employe_registry[cleaned_id]["clearance"] =="level_3":
            print("Access approved! your duty assigned at 'Quantum lab cluster'.")
        elif employe_registry[cleaned_id]["clearance"]=="level_1":
            print("Access approved! your duty assigned at 'Standard workstation'.")
        else:
            print("Access approved! your duty assigned at 'server core vault' .")
        active_tokens={"TOKEN_ALPHA","TOKEN_BETA","TOKEN_GAMMA"}
        user_token=input("Enter your current session security token code :")
        cleaned_token_code=user_token.upper()
        if  cleaned_token_code in active_tokens:
            print("Security violation : Token re-use Detected! vault lockdown initiated!")
        else:
            active_tokens.add(cleaned_token_code)
            print("Token Authorized. security handshake complete.")
    else:
        print("Access denied! Account suspended. contact security cammand center!") 
else:
    print("Access denied! Invalid Employee identity token!")
audit_logs=[]
log_entry=(user_id,employee_status,cleaned_token_code)
audit_logs.append(log_entry)
print("---SECURE SECURITY AUDIT LOG HISTORY DATA---")
print(audit_logs)