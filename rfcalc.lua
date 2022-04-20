--ez time
function tm (t)
    local t = textutils.formatTime(os.time())


--print center

local w,h =term.getSize()
	function pCen (y,s)
		local x = math.floor((w - string.len(s)) /2)
		term.setCursorPos(x,y)
		term.clearLine()
		term.write(s)
	end

local nop = 1

--draw menu

local function drawMen()
	term.clear()
	term.setCursorPos(1,1)
	term.write("RF calculator v 0.1 ")
		
	term.setCursorPos(w-11,1)
end
	
if nop == 1 then
	term.write("RF")
elseif nop == 2 then
	term.write("T")
else
end

--gui

term.clear()

local function drawFrnt()
	pCen(math.floor(h/2) - 4, "")
	pCen(math.floor(h/2) - 3, "Find")
	pCen(math.floor(h/2) - 2, "")
	pCen(math.floor(h/2) - 1, ((nop == 1 and "[RF]") or "RF"))
	pCen(math.floor(h/2) + 0, ((nop == 2 and "[T]")	or "T"))
end

--Display

drawMen()
drawFrnt()

while true do
	local e,p = os.pullEvent()
		if e == "key" then
			local key = p
			if key == 17 or key == 200 then
			if nop > 1 then
			nop = nop - 1
drawMen()
drawFrnt()
			end
		elseif key == 31 or key == 208 then
			if nop < 4 then
			nop = nop + 1
drawMen()
drawFrnt()
			end
		elseif key == 28 then
			break
		end
	end
end

term.clear()

if nop == 1 then
	shell.run("rom/rft")
elseif nop == 2 then
	print("fartbeans" .. tm(t))
end 