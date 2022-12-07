class CraneStack
    attr_reader :stacks
  
    def initialize
      @stacks =
        input[0]
        .split("\n")
        .map(&:chars)
        .transpose
        .select! { |stack| stack.any? { |e| e.match?(/\d+/) } }
        .to_h { |stack| [stack.pop, stack.reject { |e| e == " " }] }
    end
  
    def sol1
      crane do |quan, src, dest|
        quan.times { stacks[dest].unshift stacks[src].shift }
      end
    end
  
    def sol2
      crane do |quan, src, dest|
        stacks[dest].unshift(*stacks[src].shift(quan))
      end
    end
  
    private
  
    def crane
      instructions.each do |instruction|
        case instruction.split
        in ["move", quan, "from", src, "to", dest]
          yield quan.to_i, src, dest
        else
          next
        end
      end
      stacks.values.map(&:first).join
    end
  
    def instructions
      @instructions ||= input[1].lines
    end
  
    def input
      @input ||= File.read(File.join(__dir__, "input.txt")).split("\n\n")
    end
  end
  
  puts "Solution 1: #{CraneStack.new.sol1}"
  puts "Solution 2: #{CraneStack.new.sol2}"