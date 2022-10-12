#!/usr/bin/env ruby

GROUPS = [
  "generic",
  "string",
  "list",
  "set",
  "sorted_set",
  "hash",
  "pubsub",
  "transactions",
  "connection",
  "server",
  "scripting",
  "hyperloglog",
  "cluster",
  "geo",
  "stream"
].freeze

GROUPS_BY_NAME = Hash[*
  GROUPS.each_with_index.map do |n,i|
    [n,i]
  end.flatten
].freeze

def argument arg
  name = arg["name"].is_a?(Array) ? arg["name"].join(" ") : arg["name"]
  name = arg["enum"].join "|" if "enum" == arg["type"]
  name = arg["command"] + " " + name if arg["command"]
  if arg["multiple"]
    name = "#{name} [#{name} ...]"
  end
  if arg["optional"]
    name = "[#{name}]"
  end
  name
end

def arguments command
  return "-" unless command["arguments"]
  command["arguments"].map do |arg|
    argument arg
  end.join " "
end

def commands
  return @commands if @commands

  require "rubygems"
  require "net/http"
  require "net/https"
  require "json"
  require "uri"

  url = URI.parse "https://raw.githubusercontent.com/antirez/redis-doc/master/commands.json"
  client = Net::HTTP.new url.host, url.port
  client.use_ssl = true
  response = client.get url.path
  if response.is_a?(Net::HTTPSuccess)
    @commands = JSON.parse(response.body)
  else
    response.error!
  end
end

def generate_groups
  GROUPS.map do |n|
    "\"#{n}\""
  end.join(",\n    ");
end

def generate_commands
  commands.to_a.sort do |x,y|
    x[0] <=> y[0]
  end.map do |key, command|
    group = GROUPS_BY_NAME[command["group"]]
    if group.nil?
      STDERR.puts "Please update groups array in #{__FILE__}"
      raise "Unknown group #{command["group"]}"
    end

    ret = <<-SPEC
{ "#{key}",
    "#{arguments(command)}",
    "#{command["summary"]}",
    #{group},
    "#{command["since"]}" }
    SPEC
    ret.strip
  end.join(",\n    ")
end

# Write to stdout
puts <<-HELP_H
/* Automatically generated by #{__FILE__}, do not edit. */

#ifndef __REDIS_HELP_H
#define __REDIS_HELP_H

static char *commandGroups[] = {
    #{generate_groups}
};

struct commandHelp {
  char *name;
  char *params;
  char *summary;
  int group;
  char *since;
} commandHelp[] = {
    #{generate_commands}
};

#endif
HELP_H

