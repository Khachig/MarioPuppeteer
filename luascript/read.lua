function file_exists(file)

  -- Check if given file exists
  local input = io.open(file, 'rb') -- open file
  if input then input:close() end -- if file has content then close the file
  return input ~= nil -- if file is not empty, return true, else false

end


function read_file(file)

  -- Read the file and return the content
  if not file_exists(file) then return nil end -- If file exists
  lines = {} -- initialize empty table
  for line in io.lines(file) do -- loop through file
    table.insert(lines, line) -- add each line to table
  end
  return lines -- return table

end


getmetatable('').__call = string.sub -- get string splicing
filename = "commands.txt" -- file to read


while true do

  local commands = read_file(filename) -- read text file
  if commands ~= nil then -- If content is not nil
      for i = 1, #commands, 1 do -- loop through all commands
        -- convert each hex command to number and write to memory
        -- splice the string into two sections, one is the memory address and the other is the value
        memory.writebyte(tonumber(commands[i](1, 6)), tonumber(commands[i](8, 11)))
      end
  end
  os.remove(filename) -- remove file after writing commands

  emu.frameadvance() -- advance one frame

end
