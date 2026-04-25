import random,copy,math
import numpy as np
import pandas as pd

def generate_data(n=15):
    return [{"zone":i+1,"metrics":{"traffic":random.randint(50,200),"pollution":random.randint(30,150),"energy":random.randint(40,180)},"history":[random.randint(10,100) for _ in range(3)]} for i in range(n)]

def replicate_data(original):
    return original,copy.copy(original),copy.deepcopy(original)

def personalize_data(data,roll):
    return data[::-1] if int(roll[-1])%2==0 else data[3:]+data[:3]

def custom_risk_score(z):
    m=z["metrics"]
    return math.log(m["traffic"]+m["pollution"]+m["energy"])

def mutate_data(data):
    for z in data:
        z["metrics"]["traffic"]+=20
        z["metrics"]["pollution"]+=10
        z["metrics"]["energy"]+=5
        z["history"].append(random.randint(50,120))
        z["risk"]=custom_risk_score(z)

def to_dataframe(data):
    return pd.DataFrame([{"zone":z["zone"],"traffic":z["metrics"]["traffic"],"pollution":z["metrics"]["pollution"],"energy":z["metrics"]["energy"],"risk":z.get("risk",0)} for z in data])

def analyze(df):
    r=df["risk"].values
    mean,var,std=np.mean(r),np.var(r),np.std(r)
    anomalies=df[df["risk"]>mean+std]["zone"].tolist()
    high_risk=df[df["risk"]>mean]["zone"].tolist()
    return mean,var,std,anomalies,high_risk

def manual_corr(x,y):
    xm,ym=np.mean(x),np.mean(y)
    num=np.sum((x-xm)*(y-ym))
    den=math.sqrt(np.sum((x-xm)**2)*np.sum((y-ym)**2))
    return num/den if den!=0 else 0

def detect_patterns(orig_before,orig_after,df):
    corruption=orig_before[0]["metrics"]!=orig_after[0]["metrics"]
    risks=df["risk"].values
    max_risk,min_risk=np.max(risks),np.min(risks)
    stability=1/(np.var(risks)+1e-5)
    risky=df[df["risk"]>np.mean(risks)]["zone"].tolist()
    clusters=[];temp=[]
    for z in risky:
        if not temp or z==temp[-1]+1:temp.append(z)
        else:
            if len(temp)>1:clusters.append(temp)
            temp=[z]
    if len(temp)>1:clusters.append(temp)
    return corruption,(max_risk,min_risk,stability),clusters

def final_decision(stability):
    if stability>1:return "System Stable"
    elif stability>0.5:return "Moderate Risk"
    elif stability>0.2:return "High Corruption Risk"
    else:return "Critical Failure"

roll="AP24110011717"
data=generate_data()
print("BEFORE:",data)

data=personalize_data(data,roll)
assigned,shallow,deep=replicate_data(data)
orig_before=copy.deepcopy(data)

mutate_data(shallow)

print("\nAFTER (Original affected due to shallow):",data)
print("\nASSIGNED:",assigned)
print("\nSHALLOW:",shallow)
print("\nDEEP (Safe):",deep)

df=to_dataframe(data)
print("\nDATAFRAME:\n",df)

mean,var,std,anomalies,high_risk=analyze(df)
corr=manual_corr(df["traffic"].values,df["pollution"].values)

corruption,risk_tuple,clusters=detect_patterns(orig_before,data,df)
decision=final_decision(risk_tuple[2])

print("\nANOMALY ZONES:",anomalies)
print("HIGH RISK ZONES:",high_risk)
print("CLUSTERS:",clusters)
print("MANUAL CORRELATION:",corr)
print("RISK TUPLE:",risk_tuple)
print("FINAL DECISION:",decision)