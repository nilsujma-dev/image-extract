# Base image
FROM alpine:latest

# First layer
RUN echo "Layer 1: Starting build process"

# Second layer
RUN echo "Layer 2: Installing dependencies" && \
    apk add --no-cache curl

# Third layer - Add a fake AWS API key
RUN echo "Layer 3: Adding fake AWS API key" && \
    echo "AKIA4HK52OLF2AAN9KWV" > /tmp/aws_key.txt

# Layers 4-19 - Create dummy files to increase layers
RUN echo "Layer 4: Creating dummy file" && touch /tmp/file4
RUN echo "Layer 5: Creating dummy file" && touch /tmp/file5
RUN echo "Layer 6: Creating dummy file" && touch /tmp/file6
RUN echo "Layer 7: Creating dummy file" && touch /tmp/file7
RUN echo "Layer 8: Creating dummy file" && touch /tmp/file8
RUN echo "Layer 9: Creating dummy file" && touch /tmp/file9
RUN echo "Layer 10: Creating dummy file" && touch /tmp/file10
RUN echo "Layer 11: Creating dummy file" && touch /tmp/file11
RUN echo "Layer 12: Creating dummy file" && touch /tmp/file12
RUN echo "Layer 13: Creating dummy file" && touch /tmp/file13
RUN echo "Layer 14: Creating dummy file" && touch /tmp/file14
RUN echo "Layer 15: Creating dummy file" && touch /tmp/file15
RUN echo "Layer 16: Creating dummy file" && touch /tmp/file16
RUN echo "Layer 17: Creating dummy file" && touch /tmp/file17
RUN echo "Layer 18: Creating dummy file" && touch /tmp/file18
RUN echo "Layer 19: Creating dummy file" && touch /tmp/file19

# Twentieth layer - Remove the fake AWS API key
RUN echo "Layer 20: Removing fake AWS API key" && \
    rm /tmp/aws_key.txt

# Final cleanup
RUN echo "Final layer: Cleanup" && \
    rm -rf /tmp/file*

# Default command
CMD ["echo", "Docker image build complete"]

