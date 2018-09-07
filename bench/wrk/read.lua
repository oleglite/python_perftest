math.randomseed(100)

method = "GET"
headers = {}
headers["Content-Type"] = "application/json"
path = '/record/read/|RECORD_ID|'
max_id = 100000


request = function()
    local record_id = math.random(max_id)
    return wrk.format(method, string.gsub(path, "|RECORD_ID|", record_id), headers, nil)
end
