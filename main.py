from pyscript import document

gr7 = {"Carlos Aguas", "Zyren Naguit", "Brixen Rabacca"}
gr8 = {"Sean Young", "Kiel Sunga", "Andrei Viray"}
gr9 = {"John Doe", "Jane Smith", "Alice Johnson"}
gr10 = {"Michael Brown", "Emily Davis", "David Wilson"}
masterset = gr7.union(gr8, gr9, gr10)




def add_nm(event):
    fname = document.getElementById("fname").value.strip().lower()
    lname = document.getElementById("lname").value.strip().lower()
    name = fname + " " + lname
    msg = document.getElementById("msg")

    
    masterset.add(name.title())
    final = "\n".join(masterset)
    msg.innerText = f"{final} \n\nTotal: {len(masterset)}"



