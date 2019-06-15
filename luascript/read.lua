function file_exists(file)
  local input = io.open(file, 'rb') -- open file
  if input then input:close() end -- if file has content then close the file
  return input ~= nil -- if file is not empty, return true, else false
end


function read_file(file)
  -- Read the "hack.txt" file and return the content
  if not file_exists(file) then return nil end -- If file exists
  lines = {} -- initialize empty table
  for line in io.lines(file) do -- loop through file
    table.insert(lines, line) -- add each line to table
  end
  return lines -- return table
end


while true do
  emu.frameadvance() -- advance one frame
end
