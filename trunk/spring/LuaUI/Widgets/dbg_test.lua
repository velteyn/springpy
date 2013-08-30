function widget:GetInfo()
  return {
    name      = "Test widget",
    desc      = "stuff",
    author    = "",
    date      = "",
    license   = "PD",
    layer     = 0,
    enabled   = true,
  }
end

function widget:Initialize()
  local clock = os.clock()
  Spring.Echo("bla", clock)
  WG.SavePythonDict("results.py", {clock = clock}, "stuff", {endOfFile = true})
end