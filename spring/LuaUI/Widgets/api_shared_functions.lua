function widget:GetInfo()
  return {
    name      = "Shared Functions",
    desc      = "Declares global functions or constants",
    author    = "KingRaptor (L.J. Lim)",
    date      = "2013.06.13",
    license   = "Public Domain",
    layer     = -math.huge,
    enabled   = true,
  }
end

local function WriteIndents(num)
	local str = ""
	for i=1, num do
		str = str .. "\t"
	end
	return str
end

local keywords = {}

-- raw = print table key-value pairs straight to file (i.e. not as a table)
local function WritePythonDict(listName, array, numIndents, endOfFile, raw, concise)
	numIndents = numIndents or 0
	local comma = raw and "" or ","
	local separator = raw and " = " or  " : "
	local str = ""
	if not raw then
	      str = listName .. " = "	--WriteIndents(numIndents)
	      str = str .. (concise and "{" or "{\n")
	end
	for i,v in pairs(array) do
		if not raw then
			str = str .. WriteIndents(numIndents + 1)
		end
		if (type(i) == "string") and not raw then
			str = str .. string.format("%q", i) .. separator
		else
			str = str .. i .. separator
		end
		
		if type(v) == "table" then
			str = str .. WritePythonDict(v, concise and 0 or numIndents + 1, false, false, concise)
		elseif type(v) == "boolean" then
			str = str .. v and "True" or "False" .. comma .. "\n"
		elseif type(v) == "string" then
			str = str .. string.format("%q", v) .. "" .. comma .. (concise and '' or "\n")
		else
			str = str .. v .. comma .. "\n"
		end
	end
	if not raw then
		str = str ..WriteIndents(numIndents) .. "}"
	end
	if not endOfFile then
		str = str .. ",\n"
	end
	
	return str
end

WG.WritePythonDict = WritePythonDict

function WG.PrintPythonDict(f, listName, list, raw)
	file = io.open(f, "w")
	if (file== nil) then
		Spring.Log(widget:GetInfo().name, "error", "could not open file for writing!")
		return
	end
	file:write(WritePythonDict(listName, list, 0, true, raw))
	file:flush()
	file:close()
end

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
function widget:Initialize()
end
